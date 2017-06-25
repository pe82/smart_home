# smart_home
A simple proof of concept for controlling devices via web with the help of django and python.

This code works on Raspberry Pi 2. 

Here are the things you need to buy or install:

1. Raspberry Pi 2B
2. python 3
3. pip3 
4. RPi.GPIO 

Optional but required for testing: 

1. Breadboard
2. Wiring
3. 4x 100-ohm resistors
4. 4x LEDs

Run: 
python manage.py migrate
python manage.py run --sync-db (if "no such table" error)
