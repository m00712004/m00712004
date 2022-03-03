import opc
import time
import random

leds = [(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def function():
    for led in range (74, 374, 60):
        leds[led] = (255,255,255)
        time.sleep(0.1)
        client.put_pixels(leds)

function()

    

