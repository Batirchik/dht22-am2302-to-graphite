#!/bin/sh

# install C BCM2835 library
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz;
tar xvfz bcm2835-1.50.tar.gz;
cd bcm2835-1.50;
./configure;
make;
sudo make install

# install python library that works with AM2302 sensor
pip install am2302_rpi