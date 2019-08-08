#!/usr/bin/python3

# PARTY MODE!

# Fires random-hue color values to a Particle Photon-based Neopixel Lamp for a 
# color-changing effect.

import requests
import random
from time import sleep

digits=[48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70] #ASCII codes of the 16 hexadecimal digits
host = 'https://api.particle.io/v1/devices/'
device = '########################'
method = '/cheerlights'
token = '########################################'

#r = requests.post(host+device+method, data = {'access_token':token,'arg':'eeffff'})
#print(r.url)
#exit()

while(True):
  hsv = ''
  for i in range(6):
    hsv +=chr(random.choice(digits))
  print(hsv)
  data = {'access_token':token,'arg':hsv}
  try:
    r = requests.post(host+device+method, data = data)
  except:
    pass
  sleep(random.choice([1]))
exit()
