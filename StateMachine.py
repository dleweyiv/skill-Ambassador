### This program controls the state of the virtual assistant ROLL-E's animations at Villanova University
###
### Author: Noah Schwanke 		Created: 12/3/17

import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")

##############################################################################################################################
## GPIO setup

## Set numbering mode

GPIO.setmode(GPIO.BCM)

## Set pin numbers

pin1 = 26
pin2 = 19
pin3 = 13
pin4 = 6

## Set channels

# GPIO.setup(pin1, GPIO.IN)
# GPIO.setup(pin2, GPIO.IN)
# GPIO.setup(pin3, GPIO.IN)
# GPIO.setup(pin4, GPIO.IN)

## set default inputs to 0 -- should this be done in this script? Probably handled by david?

GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


defaultState = [GPIO.input(pin1),GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]  

# print defaultState ## This should be all 0's

# print(defaultState)

##############################################################################################################################
## LED Matrix config

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.gpio_slowdown = 2
options.hardware_mapping = 'regular'

sleepWaitTime = 500 	# how many seconds until sleep is activated

matrix = RGBMatrix(options = options)

##############################################################################################################################
## Importing images

sleep1 = Image.open("/home/pi/ROLLE/ROLLESleep1.png")
sleep2 = Image.open("/home/pi/ROLLE/ROLLESleep2.png")

closedmouth = Image.open("/home/pi/ROLLE/ROLLE.png")
blink = Image.open("/home/pi/ROLLE/ROLLEEyesClosed.png")

# openmouth = Image.open("ROLLEMouthOpen.png")
talking1 = Image.open("/home/pi/ROLLE/ROLLETalk1.png")
talking2 = Image.open("/home/pi/ROLLE/ROLLETalk2.png")

thinking1 = Image.open("/home/pi/ROLLE/ROLLEThinking1.png")
thinking2 = Image.open("/home/pi/ROLLE/ROLLEThinking2.png")


happy = Image.open("/home/pi/ROLLE/ROLLEHappy.png")
sad = Image.open("/home/pi/ROLLE/ROLLESad.png")
mad = Image.open("/home/pi/ROLLE/ROLLEMad.png")

nationer1 = Image.open("/home/pi/ROLLE/ROLLEVEyes1.png")
nationer2 = Image.open("/home/pi/ROLLE/ROLLEVEyes2.png")
#############################################################################################################################
## Setting states as lists

awake = [False, False, False, True]
thinking = [False, False, True, False]
talking = [False, False, True, True]
villanova = [False, True, False, False]
happyFace = [False, True, False, True]
sadFace = [False, True, True, False]
madFace = [False, True, True, True]
sleeping = [False, False, False, False]


##############################################################################################################################
## Finite State Machine 

## GPIO.wait_for_edge(##, GPIO.RISING) 
## GPIO.input(pin1):

print("\n\nEntering infinite loop..")

# Begin infinite loop of ROLL-E Animations
sleepTimer = 0
inf = 1
while (inf == 1):

	## Get value at GPIOs
	currentState = [GPIO.input(pin1),GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]

	## Set the awake animation while 0001, which is default of GPIOS
	if ((currentState[0] == awake[0]) and (currentState[1] == awake[1]) and (currentState[2] == awake[2]) and (currentState[3] == awake[3])):

		## Do I need to clear once in the beginning?
		matrix.SetImage(closedmouth.convert('RGB')) 

		time.sleep(2.5)

		matrix.Clear()

		matrix.SetImage(blink.convert('RGB'))

		time.sleep(.2)

		matrix.Clear()

		sleepTimer = sleepTimer + 2.7

		## If the script has been in this awake loop for x seconds, put into sleeping mode
		if(sleepTimer > 300):
                    
                    sleepState = [GPIO.input(pin1),GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]
                    
                    while((sleepState[0] == GPIO.input(pin1)) and (sleepState[1] == GPIO.input(pin2)) and (sleepState[2] == GPIO.input(pin3)) and (sleepState[3] == GPIO.input(pin4))):
			
            		## While the program is not equal to thinking mode to wake it up, stay sleeping

			matrix.SetImage(sleep1.convert('RGB'))

			time.sleep(.75)

			matrix.Clear()

			matrix.SetImage(sleep2.convert('RGB'))

			time.sleep(.75)

			matrix.Clear()

                    sleepTimer = 0	

		## Set the thinking animation while 0010
	if ((currentState[0] == thinking[0]) and (currentState[1] == thinking[1]) and (currentState[2] == thinking[2]) and (currentState[3] == thinking[3])):

		sleepTimer = 0
		
		matrix.SetImage(thinking1.convert('RGB'))

		time.sleep(.30)

		matrix.Clear()

		matrix.SetImage(thinking2.convert('RGB'))

		time.sleep(.30)

		matrix.Clear()


	## Set the talking animation while 0011
	if ((currentState[0] == talking[0]) and (currentState[1] == talking[1]) and (currentState[2] == talking[2]) and (currentState[3] == talking[3])):

		sleepTimer = 0

		matrix.SetImage(talking1.convert('RGB'))

		time.sleep(.25)

		matrix.Clear()

		matrix.SetImage(talking2.convert('RGB'))

		time.sleep(.25)

		matrix.Clear()


	## Set the Nationer face when 0100
	if ((currentState[0] == villanova[0]) and (currentState[1] == villanova[1]) and (currentState[2] == villanova[2]) and (currentState[3] == villanova[3])):

		sleepTimer = 0

		matrix.SetImage(nationer1.convert('RGB'))

		time.sleep(.25)

		matrix.Clear()

		matrix.SetImage(nationer2.convert('RGB'))

		time.sleep(.25)

		matrix.Clear()

	## Set the Happy face when 0101
	if ((currentState[0] == happyFace[0]) and (currentState[1] == happyFace[1]) and (currentState[2] == happyFace[2]) and (currentState[3] == happyFace[3])):

		sleepTimer=0

		matrix.SetImage(happy.convert('RGB'))

		time.sleep(.2)
		
		matrix.Clear()

	## Set the Sad face when 0110
	if ((currentState[0] == sadFace[0]) and (currentState[1] == sadFace[1]) and (currentState[2] == sadFace[2]) and (currentState[3] == sadFace[3])):

		sleepTimer=0

		matrix.SetImage(sad.convert('RGB'))

		time.sleep(.2)

		matrix.Clear()

	## Set the Mad face when 0111
	if ((currentState[0] == madFace[0]) and (currentState[1] == madFace[1]) and (currentState[2] == madFace[2]) and (currentState[3] == madFace[3])):
		
		sleepTimer=0		

		matrix.SetImage(mad.convert('RGB'))

		time.sleep(.2)

		matrix.Clear()

	 ## Set sleeping when 0000
        if ((currentState[0] == sleeping[0]) and (currentState[1] == sleeping[1]) and (currentState[2] == sleeping[2]) and (currentState[3] == sleeping[3])):

                matrix.SetImage(sleep1.convert('RGB'))

                time.sleep(1.5)

                matrix.Clear()

                matrix.SetImage(sleep2.convert('RGB'))

                time.sleep(.75)

                matrix.Clear()

                currentState = [GPIO.input(pin1),GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]
