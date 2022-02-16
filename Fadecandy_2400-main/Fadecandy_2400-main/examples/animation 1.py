import opc
import time
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(120):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[119-led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1

for led in range(120,180):
    leds[led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[179-led] = (0,255,255)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1

for led in range(180,240):
    leds[led] = (0,255,255)
    time.sleep(.01)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[239-led] = (100,20,50)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1

for led in range(240,300):
    leds[led] = (100,20,50)
    time.sleep(.01)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[299-led] = (0,255,255)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1

for led in range(300,360):
    leds[led] = (30,20,50)
    time.sleep(.01)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[359-led] = (70,255,120)
    time.sleep(.01)
    client.put_pixels(leds)
    led = led + 1
    
led = 0
while led<360:
    for rows in range(6):
        leds[led] = (255,255,255)
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1
