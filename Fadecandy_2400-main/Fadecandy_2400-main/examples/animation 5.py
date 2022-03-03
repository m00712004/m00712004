import opc
import time
import random

leds = [(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

i = (6,66,126,186,246,306)
k = (9,69,129,189,249,309,130,190,131,191,72,13,252,313)
r = (15,16,17,75,135,195,255,315,78,138,196,197,257,318)
a = (21,22,81,82,140,200,260,320,201,202,203,143,263,323)
m = (25,26,30,31,85,87,89,91,145,148,151,205,211,265,271,325,331)

def letteri():
    for led in i:
        leds[led] = (255,102,102)
        time.sleep(0.1)
        client.put_pixels(leds)

letteri()

def letterk():
    for led in k:
        leds[led] = (255,255,102)
        time.sleep(0.1)
        client.put_pixels(leds)

letterk()    

def letterr():
    for led in r:
        leds[led] = (128,255,102)
        time.sleep(0.1)
        client.put_pixels(leds)

letterr()

def lettera():
    for led in a:
        leds[led] = (102,255,255)
        time.sleep(0.1)
        client.put_pixels(leds)

lettera()

def letterm():
    for led in m:
        leds[led] = (204,102,255)
        time.sleep(0.1)
        client.put_pixels(leds)

letterm()
