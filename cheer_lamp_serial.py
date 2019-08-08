#!/usr/bin/python3

# Cheer Lamp Host

# Polls my ThingSpeak Channel for a new cheerlights color every 20 seconds, and
# updates an arduino-based neopixel lamp connected over USB via the serial port.

import requests
import serial
from time import sleep

#r = requests.get(url='http://api.thingspeak.com/channels/******/feed.json')
#print(r.json()['feeds'][0]['field1'])  #color_name
#print(r.json()['feeds'][0]['field2'])  #color_hex
ser = serial.Serial('COM21', 9600)
try:
  r = requests.get(url='http://api.thingspeak.com/channels/******/field/2/last.json')
except:
  pass

while(True):
  try:
    r = requests.get(url='http://api.thingspeak.com/channels/******/field/2/last.json')
    print(r.json()['field2'])
  except:
    continue  
  ser.write(bytes(''+r.json()['field2']+'\n',"UTF8"))
  sleep(20)
ser.close()
