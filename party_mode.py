#!/usr/bin/python3

#sudo pip install requests
import requests
import random
from time import sleep

digits=[48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70] # 0,48: 9,57: A,65: F,70
host = 'https://api.particle.io/v1/devices/'
device = '370024001147343438323536'
method = '/cheerlights'
token='a90e1edf6d3b34af0f1fd6354dd97825b4055865'

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
