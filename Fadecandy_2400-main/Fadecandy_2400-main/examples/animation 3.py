import opc
import time
import random

leds = [(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



led = 0
while led<60:
    for led in range (48):
        leds = [(0,0,0)]*360

        leds[57] = (255,255,255)
        leds[115] = (255,255,255)
        leds[119] = (255,255,255)
        leds[177] = (255,255,255)
        leds[235] = (255,255,255)
        leds[239] = (255,255,255)
        leds[297] = (255,255,255)
        leds[355] = (255,255,255)
        leds[359] = (255,255,255)

# first line     
        leds[3+led] = (25,255,0)
        leds[4+led] = (25,255,0)
        leds[5+led] = (25,255,0)
# second line
        leds[62+led] = (25,255,0)
        leds[63+led] = (255,20,25)
        leds[64+led] = (25,255,0)
        leds[65+led] = (255,20,25)
        leds[66+led] = (25,255,0)
# third line
        leds[121+led] = (25,255,0)
        leds[122+led] = (25,255,0)
        leds[123+led] = (25,255,0)
        leds[124+led] = (25,255,0)
        leds[125+led] = (25,255,0)
        leds[126+led] = (25,255,0)
        leds[127+led] = (25,255,0)
# fourth line
        leds[181+led] = (25,255,0)
        leds[182+led] = (25,255,0)
        leds[186+led] = (25,255,0)
        leds[187+led] = (25,255,0)
# fifth line
        leds[242+led] = (25,255,0)
        leds[243+led] = (25,255,0)
        leds[244+led] = (25,255,0)
        leds[245+led] = (25,255,0)
        leds[246+led] = (25,255,0)
# sixth line
        leds[301+led] = (25,255,255)
        leds[302+led] = (25,255,255)
        leds[306+led] = (25,255,255)
        leds[307+led] = (25,255,255)       
        
        client.put_pixels(leds)
        time.sleep(0.1)
    break


leds[301] = (25,255,255)
leds[302] = (25,255,255)
leds[306] = (25,255,255)
leds[307] = (25,255,255)
