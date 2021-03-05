# Reprap-Automesh
Generate dynamic Reprap automesh grid based on the size of the model. PyQT5 application to add as post-processing script in slicers.


Installation
I recommend to install everthing into a virtualenv!

cd ~/automesh
pip3 install virtualenv
virtualenv -p pyrhon3 venv
source venv/bin/activate

pip3 install -r requirements.txt

Testing
cd ~/automesh
./automesh.py <your gcode file>

Required Slicer settings

- Add a "dummy" M557 line to your GCODE start script
    
    M557 X10:10 Y10:10 P1:1  ; mesh grid dummy

- Add the following to your "After layer change GCODE"
  
    ;AFTER_LAYER_CHANGE
    ;LAYER [layer_num]
    ;LAYERHEIGHT [layer_z]

- Adding as post-processing script to your Slicer
    
    Please add the included bash script automesh.sh as your post-processing script, so that the virtualenv is activated before starting the main application.

    /path to the script/automesh.sh;
    

<img width="799" alt="main" src="https://user-images.githubusercontent.com/17797632/109992089-37d8cf00-7d0b-11eb-9f83-b407c8686bc9.png">

<img width="796" alt="result" src="https://user-images.githubusercontent.com/17797632/109953129-eebf5580-7cdf-11eb-8526-6fc16e1ae39f.png">

