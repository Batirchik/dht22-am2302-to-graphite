# Read humidity and temperature from AM2302 sensor and save to Graphite
Python script that reads the DHT series of humidity and temperature sensors on a Raspberry Pi or Beaglebone Black and saves into Grafana

In my configuration this script works with AM2302 and Raspberry Pi 3, but it may also work with Raspberry Pi 2. The main problem is to make BCM2835 C library compile and work correctly.

# Installation

Update `src/settings.py` with your configuration of Graphite.

Run `sh setup.sh` compile and install dependencies

NOTE: if you see some crazy compilation errors, than most likely bcm2835 library doesn't work with your hardware. Try to google "bcm2835 <your raspberry version>" for solution. 

# How to run

`python src/run.py`

The script itself has schedule, so you don't need to add it to crontab. I run it in background using nohub and run it on system statup.

## Register as a service

http://devopspy.com/linux/python-script-linux-systemd-service/