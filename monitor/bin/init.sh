#!/bin/bash
# init script to add system and python deps for SkyWeather2
# use sudo raspi-config
# enable ssh I2C Serial

# TODO remove stuff...

# system deps
sudo apt install i2c-tools pigpio python3-pip git

# python deps
sudo python3 -m pip install i2cdevice gpiozero pigpio smbus pyserial

mkdir src
cd src

# pi hat and loudness sensor
# https://github.com/Seeed-Studio/grove.py
git clone git@github.com:Seeed-Studio/grove.py

cd grove.py

sudo python3 -m pip install .

cd ..

# temp humidity sensor
# can this be installed?
# https://github.com/switchdoclabs/SDL_Pi_SHT30
git clone git@github.com:switchdoclabs/SDL_Pi_SHT30.git
