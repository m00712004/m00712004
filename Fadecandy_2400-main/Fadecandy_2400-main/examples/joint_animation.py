import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
print(leds)
while True:
    print("Which animation would you like to display?")
    print("a. name function")
    print("b. criss cross")
    print("c. race")
    print("d. middlesex")
    print("e. rainbow")

    x = input()

    if x == "a":
            
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
                        
                
          
    elif x == "b":
        leds=[(255,75,0)]*360

        client = opc.Client('localhost:7890')

        for item in enumerate(leds):
            time.sleep(0.006)
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


 
    elif x == "c":
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

        led = 0
        while led<60:
            for rows in range(3):
                leds[led+rows*60] = (200,0,0)
            for rows in range(3,6):
                leds[59-led + rows*60] = (rows*10,40,180)
            client.put_pixels(leds)
            time.sleep(.1)
            led = led + 1


                   
    elif x == "d":
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
                
                     
    elif x == "e":
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
            
        led = 0
        i = 0
        while led<60:
            led in range (i, 360, 60)
            leds[led] = (255,255,255)
            time.sleep(0.1)
            client.put_pixels(leds)
            i = i+1

                
        
             
    else:
        print("invalid input.")             

                 

