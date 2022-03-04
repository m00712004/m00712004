import opc
import time

leds=[(255,75,0)]*360

client = opc.Client('localhost:7890')

for item in enumerate(leds):
    time.sleep(0.01)
    if item[0]%2 == 0:
        r, g, b = item[1]
        r = r-200
        g = 25
        b = 5
       
        new_colour =(r,g,b)
        leds[item[0]]= new_colour
    client.put_pixels(leds)
    client.put_pixels(leds)

client.put_pixels(leds)
client.put_pixels(leds)
print (leds)


#sweep from right to left
led = 0
while led<360:
    for rows in range(6):
        leds[led] = (0,0,25)
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1
#cross from right to left
for led in range (5,359,59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (11, 364, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (17, 370, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (23, 375, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (29, 380, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (35, 385, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (41, 390, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (47, 395, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (53, 400, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (59, 405, 59):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)


#cross from left to right

for led in range (0,306,61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (6, 312, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (12, 318, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (18, 324, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (24, 330, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (30, 336, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (36, 342, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (42, 348, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (48, 354, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)

for led in range (54, 360, 61):
    leds[led] = (255,255,255)
    time.sleep(0.01)
    client.put_pixels(leds)





