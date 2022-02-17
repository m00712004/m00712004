import opc
import time

leds=[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

for led in range (74, 374, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
    
for led in range (135, 197, 61):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[137] = (255,255,255)
client.put_pixels(leds)
    
for led in range (78, 378, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
#i
for led in range (80, 380, 60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
#d
for led in range (82, 382, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[83] = (255,255,255)
leds[323] = (255,255,255)
client.put_pixels(leds)

for led in range (144, 322, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
#d
for led in range (86, 386, 60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[87] = (255,0,0)
leds[327] = (255,0,0)
client.put_pixels(leds)


for led in range (148, 326, 60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
#l
for led in range (90, 390, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[331] = (255,255,255)
leds[332] = (255,255,255)
client.put_pixels(leds)
#e
for led in range (94, 394, 60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[95] = (255,0,0)
leds[96] = (255,0,0)
leds[215] = (255,0,0)
leds[216] = (255,0,0)
leds[335] = (255,0,0)
leds[336] = (255,0,0)
client.put_pixels(leds)

#s
for led in range (98, 278, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

for led in range (220, 380, 60):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[99] = (255,255,255)
leds[100] = (255,255,255)
leds[219] = (255,255,255)
leds[338] = (255,255,255)
leds[339] = (255,255,255)
client.put_pixels(leds)

#e

for led in range (102, 402, 60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)

leds[103] = (255,0,0)
leds[104] = (255,0,0)
leds[223] = (255,0,0)
leds[224] = (255,0,0)
leds[343] = (255,0,0)
leds[344] = (255,0,0)
client.put_pixels(leds)

#x

for led in range (106, 406, 61):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)

for led in range (111, 401, 59):
    leds[led] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)





















    
















































