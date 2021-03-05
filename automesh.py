#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import os
import re
import sys
import math
import os.path
import base64
import collections
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt
from form_ui import Ui_MainWindow
from PyQt5.QtCore import QThread, QSettings
from PyQt5 import QtWidgets, QtCore
from pyqtspinner.spinner import WaitingSpinner
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

plt.switch_backend('Agg')

POWER_ZERO = 1

Element = collections.namedtuple('Element', ['x0', 'y0', 'x1', 'y1', 'z'])

class MainWindow(QMainWindow, Ui_MainWindow):
    done = QtCore.pyqtSignal(object, object, object, object)

    def __init__(self, filename):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.textBrowserResult.hide()
        self.pushButtonExit.hide()

        self.thread = QtCore.QThread()
        self.proc = WaitingSpinner(self, roundness=70.0, opacity=25.0, fade=50.0, radius=20.0, lines=30, line_length=50.0, line_width=5.0, speed=1.0, color=(24, 30, 255))
        #self.proc.moveToThread(self.thread)
        self.proc.start()

        self.filename = filename

        self.pushButtonExitLeft.clicked.connect(self.exit)
        self.pushButtonStart.clicked.connect(self.generateMesh)
        self.checkBoxAutoExit.clicked.connect(self.setAutoExit)
        self.xSpinBox.valueChanged.connect(self.changeX)
        self.ySpinBox.valueChanged.connect(self.changeY)

        self.labelFilename.setText(os.path.basename(self.filename))

        self.tabWidget.setTabText(0, 'Meshgrid')
        self.tabWidget.setTabText(1, 'Help')
        self.tabWidget.setTabText(2, 'About')

        self.getSettings()

        if self.settings.value('autoExit') == 1:
            self.pushButtonExit.hide()

        try:
            self.file = open(self.filename, encoding='utf-8')
        except TypeError:
            try:
                self.file = open(self.filename)
            except:
                self.textBrowserResult.append("Open file exception. Exiting meshgrid.py.")
                self.textBrowserResult.show()
        except FileNotFoundError:
            self.textBrowserResult.append('File not found. Exiting meshgrid.py.')
            self.textBrowserResult.show()

        self.lines = self.file.readlines()
        self.file.close()

        self.tnStart = 0
        self.tnData = ""

        for line in self.lines:
            if line.startswith('; thumbnail begin'):
                self.tnStart = 1
                continue
            if line.startswith('; thumbnail end'):
                self.tnStart = 0
                continue
            if self.tnStart == 1:
                self.tnData += line

        lens = len(self.tnData)
        lenx = lens - (lens % 4 if lens % 4 else 4)
        self.tnData = base64.b64decode(self.tnData.replace('; ', '')[:lenx])

        self.plot()

    def getSettings(self):
        self.settings = QSettings('maziggy', 'automesh')

        if self.settings.value('autoExit'):
            self.autoExit = self.settings.value('autoExit')
            self.checkBoxAutoExit.setChecked(True)
            self.autoExit = 1
        else:
            self.checkBoxAutoExit.setChecked(False)
            self.autoExit = 0

    def setAutoExit(self):
        if self.checkBoxAutoExit.checkState() == 2:
            self.autoExit = 1
            self.settings.setValue('autoExit', 1)
        else:
            self.autoExit = 0
            self.settings.setValue('autoExit', 0)

    def plot(self):
        self.bounds = self.findBounds()

        self.worker = GcodeReader(self.lines, self.xSpinBox.value(), self.ySpinBox.value(), self.bounds)
        self.worker.start()

        self.worker.done.connect(self.showPlot)

    def showPlot(self, fig=0, ax=0, xpoints=0, ypoints=0, restart=0):
        if restart == 0:
            self.fig = fig
            self.ax = ax
            self.xpoints = xpoints
            self.ypoints = ypoints

            self.canvas = FigureCanvas(self.fig)

            layout = QVBoxLayout()
            layout.addWidget(self.canvas)

            self.labelImage.setLayout(layout)

            self.canvas.draw()

            self.proc.stop()
            self.proc.hide()

        else:
            self.proc.start()
            self.proc.show()
            self.worker.refresh.emit(self.xSpinBox.value(), self.ySpinBox.value())
            self.proc.stop()
            self.proc.hide()
            self.canvas.draw()

    def axisEqual3D(ax):
        extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        sz = extents[:, 1] - extents[:, 0]
        centers = np.mean(extents, axis=1)
        maxsize = max(abs(sz))
        r = maxsize / 4
        for ctr, dim in zip(centers, 'xyz'):
            getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

    def changeX(self):
        self.showPlot(restart=1)

    def changeY(self):
        self.showPlot(restart=1)

    def generateMesh(self):
        self.pushButtonStart.hide()

        self.labelImage.hide()

        self.textBrowserResult.show()
        self.textBrowserResult.verticalScrollBar().setEnabled(True)
        self.textBrowserResult.verticalScrollBar().show()
        self.textBrowserResult.verticalScrollBar().setValue(self.textBrowserResult.verticalScrollBar().maximum())
        self.error = 0

        if self.settings.value('autoExit') == 1:
            self.pushButtonExit.hide()
        else:
            self.pushButtonExit.show()
            self.pushButtonExit.setEnabled(True)
            self.pushButtonExit.clicked.connect(self.exit)

        self.linesNew = self.calcBed()

        self.FileNew = open(self.filename, "r+")

        self.FileNew.seek(0)

        self.FileNew.truncate()

        for element in self.linesNew:
            self.FileNew.write(element)

        self.FileNew.close()

        if self.error == 1:
            self.textBrowserResult.setStyleSheet('color: rgb(255, 38, 0);')
        else:
            self.textBrowserResult.setStyleSheet('color: rgb(0, 0, 0);')

        if self.settings.value('autoExit') == 1:
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.exit)
            self.timer.start(2000)

    def calcBed(self):
        self.bed = self.findBed()

        for axis in self.bounds:
            if self.bounds[axis]['max'] - self.bounds[axis]['min'] < self.bed[axis]:
                self.textBrowserResult.append(f'Success: {axis} mesh is smaller than bed')
                self.textBrowserResult.show()
            else:
                self.textBrowserResult.append('Error: Mesh is larger than bed. Exiting meshgrid.py.')
                self.textBrowserResult.show()

            for limit in self.bounds[axis]:
                if limit == 'min':
                    if self.bed[axis] - self.bounds[axis][limit] > 0:
                        self.textBrowserResult.append(f"Success: {axis} {limit} {self.bounds[axis]['min']} coordinate is on the bed.")
                    else:
                        self.error = 1
                        self.textBrowserResult.setText(f'Error: {axis} {limit} coordinate is off the bed. Exiting meshgrid.py.')
                        self.textBrowserResult.show()
                if limit == 'max':
                    if (self.bed[axis]) - self.bounds[axis][limit] > 0:
                        self.textBrowserResult.append(f"Success: {axis} {limit} {self.bounds[axis]['max']} coordinate is on the bed.")
                    else:
                        self.error = 1
                        self.textBrowserResult.append(f'Error: {axis} {limit} coordinate is off the bed. Exiting meshgrid.py.')

        return self.fillGrid(self.bounds)

    def findBed(self):
        self.bed = {
            'X': 330,
            'Y': 330,
            }

        for line in self.lines:
            if line.startswith(';   strokeXoverride,'):
                self.bed['X'] = int(re.search(r'\d.+\S', line).group())
            elif line.startswith(';   strokeYoverride,'):
                self.bed['Y'] = int(re.search(r'\d.+', line).group())
                break

        return self.bed

    def findBounds(self):
        self.bounds = {
            'X': {'min': 9999, 'max': 0},
            'Y': {'min': 9999, 'max': 0},
            }

        self.parsing = False

        for line in self.lines:
            if line.startswith('; LAYER 0') or line.startswith(';LAYER 0'):
                self.parsing = True
                continue
            elif line.startswith('; LAYER 1') or line.startswith(';LAYER 1'):
                break

            if self.parsing:
                for match in re.findall(r'G1 X([\d+.]+) Y([\d+.]+).*', line):
                    self.valueX = round(float(match[0]))
                    self.valueY = round(float(match[1]))

                    self.bounds['X']['min'] = math.floor(min(self.bounds['X']['min'], self.valueX))
                    self.bounds['X']['max'] = math.ceil(max(self.bounds['X']['max'], self.valueX))
                    self.bounds['Y']['min'] = math.floor(min(self.bounds['Y']['min'], self.valueY))
                    self.bounds['Y']['max'] = math.ceil(max(self.bounds['Y']['max'], self.valueY))

        return self.bounds

    def fillGrid(self, bounds):
        self.gridNew = 'M557 X%d:%d Y%d:%d P%d:%d' % (
            self.bounds['X']['min'], self.bounds['X']['max'],
            self.bounds['Y']['min'], self.bounds['Y']['max'],
            self.xSpinBox.value(), self.ySpinBox.value()
        )

        self.linesNew = []

        for line in self.lines:
                if line.startswith('M107'):
                    continue
                elif line.startswith('M557'):
                    self.linesNew.append(re.sub(r'^M557 X\d+:\d+ Y\d+:\d+ P\d+:\d+', self.gridNew, line, flags=re.MULTILINE))
                    self.textBrowserResult.append('\n\nNew meshgrid line inserted.\n\n' + re.sub(r'^M557 X\d+:\d+ Y\d+:\d+ P\d+:\d+', self.gridNew, line, flags=re.MULTILINE))
                    continue
                else:
                    self.linesNew.append(line)

        return self.linesNew

    def exit(self):
        self.close()

class LayerError(Exception):
    pass

class GcodeType(Enum):
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

class GcodeReader(QThread):
    refresh = QtCore.pyqtSignal(object, object)
    done = QtCore.pyqtSignal(object, object, object, object)

    def __init__(self, lines, xspace, yspace, bounds, layer=1):
        QThread.__init__(self)

        self.refresh.connect(self.update)

        self.layer = layer
        self.bounds = bounds
        self.lines = lines
        self.xspace = xspace
        self.yspace = yspace
        self.n_segs = 0  # number of line segments
        self.segs = None  # list of line segments [(x0, y0, x1, y1, z)]
        self.n_layers = 0  # number of layers
        self.seg_index_bars = []
        self.subpath_index_bars = []
        self.summary = None
        self.lengths = None
        self.subpaths = None
        self.xyzlimits = None
        self.elements = None
        self.elements_index_bars = []

    def run(self):
        self._read()
        self.plot_layer(self.bounds, layer=1)

    def mesh(self, max_length):
        self.elements = []
        self.elements_index_bars = []
        bar = 0
        n_eles = 0

        for i, (x0, y0, x1, y1, z) in enumerate(self.segs):
            if i == self.seg_index_bars[bar]:
                bar += 1
                self.elements_index_bars.append(n_eles)

            length = np.hypot(x0 - x1, y0 - y1)
            n_slices = int(np.ceil(length / max_length))
            n_eles += n_slices
            dx = (x1 - x0) / n_slices
            dy = (y1 - y0) / n_slices
            for _ in range(n_slices - 1):
                self.elements.append(Element(x0, y0, x0 + dx, y0 + dy, z))
                x0, y0 = x0 + dx, y0 + dy
            self.elements.append(Element(x0, y0, x1, y1, z))
        self.elements_index_bars.append(n_eles)

        print("Meshing finished, {:d} elements generated".
              format(len(self.elements)))

    def _read(self):
        self._read_fdm_regular()
        self.xyzlimits = self._compute_xyzlimits(self.segs)

    def _compute_xyzlimits(self, seg_list):
        xmin, xmax = float('inf'), -float('inf')
        ymin, ymax = float('inf'), -float('inf')
        zmin, zmax = float('inf'), -float('inf')
        for x0, y0, x1, y1, z in seg_list:
            xmin = min(x0, x1) if min(x0, x1) < xmin else xmin
            ymin = min(y0, y1) if min(y0, y1) < ymin else ymin
            zmin = z if z < zmin else zmin
            xmax = max(x0, x1) if max(x0, x1) > xmax else xmax
            ymax = max(y0, y1) if max(y0, y1) > ymax else ymax
            zmax = z if z > zmax else zmax
        return (xmin, xmax, ymin, ymax, zmin, zmax)

    def _read_fdm_regular(self):
        skipLayer = 1
        linesTemp = []

        for line in self.lines:
            if line.startswith(';LAYER 0'):
                skipLayer = 0
            if line.startswith(';LAYER 1'):
                skipLayer = 1
            if skipLayer == 0:
                linesTemp.append(line)

        new_lines = []
        for line in linesTemp:
            if line.startswith('G'):
                idx = line.find(';')
                if idx != -1:
                    line = line[:idx]
                new_lines.append(line)
        lines = new_lines
        self.segs = []
        temp = -float('inf')
        gxyzef = [temp, temp, temp, temp, temp, temp]
        d = dict(zip(['G', 'X', 'Y', 'Z', 'E', 'F'], range(6)))
        seg_count = 0
        mx_z = -math.inf
        for line in lines:
            if not line.startswith('G1 '):
                continue
            old_gxyzef = gxyzef[:]
            for token in line.split():
                gxyzef[d[token[0]]] = float(token[1:])
            """
            # if gxyzef[3] > old_gxyzef[3]:  # z value
            # it may lift z in the beginning or during the printing process
            if gxyzef[4] > old_gxyzef[4] and gxyzef[3] > mx_z:
                mx_z = gxyzef[3]
                # print(gxyzef[3], old_gxyzef[3])
                self.n_layers += 1
                self.seg_index_bars.append(seg_count)
            """
            if (gxyzef[0] == 1 and gxyzef[1:3] != old_gxyzef[1:3]
                    and gxyzef[3] == old_gxyzef[3]
                    and gxyzef[4] > old_gxyzef[4]):
                if gxyzef[3] > mx_z:
                    mx_z = gxyzef[3]
                    self.n_layers += 1
                    self.seg_index_bars.append(seg_count)
                x0, y0, z = old_gxyzef[1:4]
                x1, y1 = gxyzef[1:3]
                self.segs.append((x0, y0, x1, y1, z))
                seg_count += 1
        self.n_segs = len(self.segs)
        self.segs = np.array(self.segs)
        self.seg_index_bars.append(self.n_segs)
        assert(len(self.seg_index_bars) - self.n_layers == 1)

    def _compute_subpaths(self):
        if not self.subpaths:
            self.subpaths = []
            self.subpath_index_bars = [0]
            x0, y0, x1, y1, z = self.segs[0, :]
            xs, ys, zs = [x0, x1], [y0, y1], [z, z]
            mx_z = zs[-1]
            for x0, y0, x1, y1, z in self.segs[1:, :]:
                if x0 != xs[-1] or y0 != ys[-1] or z != zs[-1]:
                    self.subpaths.append((xs, ys, zs))
                    if z > mx_z:
                        mx_z = z
                        self.subpath_index_bars.append(len(self.subpaths))
                    xs, ys, zs = [x0, x1], [y0, y1], [z, z]
                else:
                    xs.append(x1)
                    ys.append(y1)
                    zs.append(z)
            if len(xs) != 0:
                self.subpaths.append((xs, ys, zs))
            self.subpath_index_bars.append(len(self.subpaths))

    def plot_layer(self, bounds, layer=1, ax=None):
        self.bounds = bounds
        """ plot a specific layer in 2D """
        if layer < 0 or layer > self.n_layers:
            raise LayerError("Layer number is invalid!")
        self._compute_subpaths()
        if not hasattr(self, 'powers'):
            self.powers = [POWER_ZERO + 10] * len(self.segs)
        if not ax:
            self.fig, self.ax = create_axis(projection='2d')

        left, right = (self.seg_index_bars[layer - 1],
                self.seg_index_bars[layer])
        for (x1, y1, x2, y2, z), power in zip(self.segs, self.powers):
            self.ax.plot([x1, x2], [y1, y2], 'r-', color='blue')

        self.xmin = self.bounds['X']['min']
        self.xmax = self.bounds['X']['max']
        self.ymin = self.bounds['Y']['min']
        self.ymax = self.bounds['Y']['max']

        self.xlen = self.xmax - self.xmin
        self.ylen = self.ymax - self.ymin

        self.xs = self.xlen / (self.xspace - 1)
        self.ys = self.ylen / (self.yspace - 1)

        self.xpos = self.xmin
        xpoints = []

        while self.xpos <= self.xmax:
            xpoints.append(self.xpos)
            self.xpos = int(self.xpos + self.xs)

        self.ypos = self.ymin
        ypoints = []

        while self.ypos <= self.ymax:
            ypoints.append(self.ypos)
            self.ypos = int(self.ypos + self.ys)

        for xp in xpoints:
            for yp in ypoints:
                self.xline = self.ax.plot(xp, yp, marker='.', linestyle='', color='r', markersize='15', gid='xline' )

        for yp in ypoints:
            for xp in xpoints:
                self.yline = self.ax.plot(xp, yp, marker='.', linestyle='', color='r', markersize='15', gid='yline')

        self.ax.axis('auto')

        self.ax.set_xticks(xpoints)
        self.ax.set_yticks(ypoints)

        plt.rcParams.update({'font.size': 10})

        plt.grid(b=True, which='both', color='r', linestyle='dotted', linewidth=1)

        for tick in self.ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(10)

        for tick in self.ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(10)

        self.ax.set_title("Object size " + str(self.xlen) + " x " + str(self.ylen))

        self.done.emit(self.fig, self.ax, xpoints, ypoints)

    def update(self, xspace, yspace):
        self.xspace = xspace
        self.yspace = yspace

        self.ax.clear()

        for (x1, y1, x2, y2, z), power in zip(self.segs, self.powers):
            self.ax.plot([x1, x2], [y1, y2], 'r-', color='blue')

        xs = self.xlen / (self.xspace - 1)
        ys = self.ylen / (self.yspace - 1)

        xpos = self.xmin
        xpoints = []

        while xpos <= self.xmax:
            xpoints.append(xpos)
            xpos = int(xpos + xs)

        ypos = self.ymin
        ypoints = []

        while ypos <= self.ymax:
            ypoints.append(ypos)
            ypos = int(ypos + ys)

        for xp in xpoints:
            for yp in ypoints:
                self.ax.plot(xp, yp, marker='.', linestyle='', color='r', markersize='15')

        for yp in ypoints:
            for xp in xpoints:
                self.ax.plot(xp, yp, marker='.', linestyle='', color='r', markersize='15')

        self.ax.axis('auto')
        self.ax.set_xticks(xpoints)
        self.ax.set_yticks(ypoints)

        plt.rcParams.update({'font.size': 10})

        for tick in self.ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(10)

        for tick in self.ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(10)

        self.ax.set_title("Object size " + str(self.xlen) + " x " + str(self.ylen))

        return self.fig, self.ax

def create_axis(figsize=(8, 8), projection='2d'):
    projection = projection.lower()
    if projection not in ['2d', '3d']:
        raise ValueError

    fig, ax = plt.subplots(figsize=figsize)

    return fig, ax

def main(filename):
    global app
    app = QApplication(sys.argv)
    main_window = MainWindow(filename)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    if sys.argv[0]:
        main(sys.argv[1])
    else:
        print("ERROR: no GCODE file given!")
        sys.exit
