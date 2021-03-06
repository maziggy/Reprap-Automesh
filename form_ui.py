# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PsAutoMesh/form.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 633)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(148, 33, 146);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 90, 81, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.xLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.xLabel.setObjectName("xLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.xLabel)
        self.yLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yLabel.setObjectName("yLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.yLabel)
        self.xSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.xSpinBox.setMinimum(2)
        self.xSpinBox.setMaximum(20)
        self.xSpinBox.setProperty("value", 4)
        self.xSpinBox.setDisplayIntegerBase(10)
        self.xSpinBox.setObjectName("xSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xSpinBox)
        self.ySpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.ySpinBox.setMinimum(2)
        self.ySpinBox.setMaximum(20)
        self.ySpinBox.setProperty("value", 4)
        self.ySpinBox.setObjectName("ySpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ySpinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 40, 20, 591))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.labelFilename = QtWidgets.QLabel(self.centralwidget)
        self.labelFilename.setGeometry(QtCore.QRect(160, 20, 611, 16))
        self.labelFilename.setObjectName("labelFilename")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(10, 170, 91, 32))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonExitLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExitLeft.setGeometry(QtCore.QRect(10, 220, 91, 32))
        self.pushButtonExitLeft.setMouseTracking(False)
        self.pushButtonExitLeft.setFlat(False)
        self.pushButtonExitLeft.setObjectName("pushButtonExitLeft")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(130, 50, 661, 581))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtWidgets.QWidget()
        self.tabMain.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabMain.setObjectName("tabMain")
        self.labelImage = QtWidgets.QLabel(self.tabMain)
        self.labelImage.setGeometry(QtCore.QRect(1, 0, 661, 551))
        self.labelImage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.textBrowserResult = QtWidgets.QTextBrowser(self.tabMain)
        self.textBrowserResult.setEnabled(False)
        self.textBrowserResult.setGeometry(QtCore.QRect(0, 0, 661, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowserResult.setFont(font)
        self.textBrowserResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowserResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowserResult.setLineWidth(3)
        self.textBrowserResult.setObjectName("textBrowserResult")
        self.pushButtonExit = QtWidgets.QPushButton(self.tabMain)
        self.pushButtonExit.setEnabled(False)
        self.pushButtonExit.setGeometry(QtCore.QRect(250, 510, 113, 32))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.textBrowserResult.raise_()
        self.labelImage.raise_()
        self.pushButtonExit.raise_()
        self.tabWidget.addTab(self.tabMain, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.label_3 = QtWidgets.QLabel(self.tabSettings)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabSettings)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabSettings)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tabSettings)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.autoExitLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.autoExitLabel.setObjectName("autoExitLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.autoExitLabel)
        self.autoExitCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.autoExitCheckBox.setObjectName("autoExitCheckBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.autoExitCheckBox)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tabSettings)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 461, 77))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.autoUploadLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.autoUploadLabel.setObjectName("autoUploadLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.autoUploadLabel)
        self.autoUploadCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.autoUploadCheckBox.setObjectName("autoUploadCheckBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.autoUploadCheckBox)
        self.printerURLLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.printerURLLabel.setObjectName("printerURLLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.printerURLLabel)
        self.printerURLLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.printerURLLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.printerURLLineEdit.sizePolicy().hasHeightForWidth())
        self.printerURLLineEdit.setSizePolicy(sizePolicy)
        self.printerURLLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.printerURLLineEdit.setObjectName("printerURLLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.printerURLLineEdit)
        self.labelDwcUrl = QtWidgets.QLabel(self.tabSettings)
        self.labelDwcUrl.setGeometry(QtCore.QRect(470, 200, 131, 16))
        self.labelDwcUrl.setObjectName("labelDwcUrl")
        self.tabWidget.addTab(self.tabSettings, "")
        self.tabHelp = QtWidgets.QWidget()
        self.tabHelp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabHelp.setObjectName("tabHelp")
        self.textBrowser = QtWidgets.QTextBrowser(self.tabHelp)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 651, 551))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tabHelp, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabAbout.setObjectName("tabAbout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tabAbout)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 651, 551))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tabAbout, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reprap Auto Meshgrid Generator"))
        self.xLabel.setText(_translate("MainWindow", "X"))
        self.yLabel.setText(_translate("MainWindow", "Y"))
        self.label.setText(_translate("MainWindow", "Probe Points"))
        self.label_2.setText(_translate("MainWindow", "File:"))
        self.labelFilename.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonStart.setText(_translate("MainWindow", "Do It!"))
        self.pushButtonExitLeft.setText(_translate("MainWindow", "Exit"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Tab 1"))
        self.label_3.setText(_translate("MainWindow", "Settings"))
        self.label_4.setText(_translate("MainWindow", "General"))
        self.label_5.setText(_translate("MainWindow", "Upload"))
        self.autoExitLabel.setText(_translate("MainWindow", "Auto Exit"))
        self.autoUploadLabel.setText(_translate("MainWindow", "AutoUpload"))
        self.printerURLLabel.setText(_translate("MainWindow", "Duet DWC URL"))
        self.printerURLLineEdit.setText(_translate("MainWindow", "https://"))
        self.labelDwcUrl.setText(_translate("MainWindow", "/machine/file/gcodes/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Page"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:xx-large; font-weight:600;\"><br /></h1>\n"
"<h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Reprap-Automesh</span></h1>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Generate dynamic Reprap automesh grid based on the size of the model. PyQT5 application to add as post-processing script in slicers.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Prerequisites</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">python3</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pip3</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">numpy==1.20.1</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pandas==1.2.3</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">matplotlib==3.3.4</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyQt5==5.15.3</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Installation I recommend to install everthing into a virtualenv!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cd ~/automesh pip3 install virtualenv virtualenv -p pyrhon3 venv source venv/bin/activate</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pip3 install -r requirements.txt</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Testing cd ~/automesh ./automesh.py </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Required Slicer settings</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-weight:600; text-decoration: underline;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add a &quot;dummy&quot; M557 line to your GCODE start script</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-style:italic;\">M557 X10:10 Y10:10 P1:1 ; mesh grid dummy</span></p>\n"
"<li style=\" font-style:italic;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add the following to your &quot;After layer change GCODE&quot;</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">;AFTER_LAYER_CHANGE <br />;LAYER [layer_num] <br />;LAYERHEIGHT [layer_z]</p>\n"
"<li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adding as post-processing script to your Slicer</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Please add the included bash script automesh.sh as your post-processing script, so that the virtualenv is activated before starting the main application.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">/path to the script/automesh.sh;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHelp), _translate("MainWindow", "Page"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">ABOUT</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Homepage: https://github.com/maziggy/Reprap-Automesh</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("MainWindow", "Tab 2"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
