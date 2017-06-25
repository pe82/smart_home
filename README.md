# smart_home
A simple proof of concept for controlling devices via web with the help of django and python.

This code was developed and ran on Raspberry Pi 2B, but it can be adapted to use Raspberry Pi 3 (just change the GPIO pins in the view). 

Here are the things you need to buy or install:

1. Raspberry Pi 2B (http://amzn.to/2t81DCl) or Raspberry Pi 3 (http://amzn.to/2t4A24P)
2. python 3
3. pip3 
4. RPi.GPIO (run: pip3 install RPi.GPIO)

Optional but required for testing: 

1. Breadboard (from this kit: http://amzn.to/2sE72zU)
2. Wiring (from this kit: http://amzn.to/2sE72zU)
3. 4x 100-ohm resistors (from this kit: http://amzn.to/2s4oA9J)
4. 4x LEDs (from this kit: http://amzn.to/2s4oA9J)

Run: 
python manage.py migrate
python manage.py run --sync-db (if "no such table" error)
