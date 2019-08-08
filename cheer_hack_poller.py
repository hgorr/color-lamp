#! /usr/bin/env python3

#check ya cheer!

# Runs on Raspberry Pi 1B+/2B/3B with SenseHat installed
# Every 10 seconds, poll the official cheerlights ThingSpeak channel (1417). If the 
# color has changed, fire the proper ThingHTTP request to update the color on my
# personal ThingSpeak channel, which stores the colors as HSV instead of RGB. 
# Also change the color of the SenseHat's RGB matrix to match the current color.

cheerlights_url = 'http://api.thingspeak.com/channels/1417/field/1/last.json'
rgb_url = 'http://api.thingspeak.com/channels/1417/field/2/last.json'
cheerhack_url = 'https://api.thingspeak.com/apps/thinghttp/send_request?api_key='
color_names =	 ['red','green','blue','cyan','white','oldlace','warmwhite','purple','magenta','yellow','orange','pink']
rgbs =	 		 ['FF0000','008000','0000FF','00FFFF','FFFFFF','FDF5E6','FDF5E6','800080','FF00FF','FFFF00','FFA500','FFC0CB']
color_api_keys = ['****************','****************','****************','****************','****************','****************','****************','****************','****************','****************','****************','****************']
poll_delay_seconds = 10

from sense_hat import SenseHat
from time import sleep
import requests

sense = SenseHat()
current_color=''

while(True):
  try:
    new_color = requests.get(cheerlights_url).json()['field1']
    new_rgb = requests.get(rgb_url).json()['field2']
    index = color_names.index(new_color)
    if index > -1:
      if not(new_color == current_color):
        current_color = new_color
        requests.get(cheerhack_url+color_api_keys[index])
        r = int(rgbs[index][0:2],16)
        g = int(rgbs[index][2:4],16)
        b = int(rgbs[index][4:6],16)
        sense.clear(r,g,b)
        print('Changing Cheerlights to: ' + current_color,r,g,b)
  except:
    pass
  sleep(poll_delay_seconds)

