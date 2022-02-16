#!/usr/bin/env python

import opc
import time

leds=[(255,75,0)]*360

client = opc.Client('localhost:7890')

print (enumerate(leds))
for item in enumerate(leds):
    time.sleep(0.006)
    print (item)
    if item[0]%2 == 0:
        #need to get values out of tuple
        r, g, b = item[1]
        r = r-200
        g = 25
        b = 5
       


        #create changed tuple (uses some values from old and some new) 
        new_colour =(r,g,b)
        leds[item[0]]= new_colour
    client.put_pixels(leds)
    client.put_pixels(leds)

client.put_pixels(leds)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(leds)
print (leds)

led = 0
while led<360:
    for rows in range(6):
        leds[led] = (0,0,25)
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1
