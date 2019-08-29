# SCRIPT POUR RADAR DE DISTANCE

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


GPIO.setup(16,GPIO.OUT) # TRIG
GPIO.setup(22,GPIO.IN) # ECHO

GPIO.output(16,False)

#repet = input("Entrez un nombre de repetitions de mesure : ")
def start(win):
    beginning = time.time()
    for x in range(50):
        time.sleep(1)

        GPIO.output(16,True)
        time.sleep(0.0001)
        GPIO.output(16,False)

        while GPIO.input(22)==0:
            debutImpulsion = time.time()

        while GPIO.input(22)==1:
            finImpulsion = time.time()

        distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)

        minDist = 5.0
        maxDist = minDist + 10.0

        if distance > minDist and distance < maxDist:
            print("Tu es as", distance, "cm depuis", int(time.time() - beginning), "secondes!")
            if time.time() > beginning + 5.0:
                print("Bonne distance!")
                return "OK"
                exit()

        else:
            print("Tu es as ", distance, "cm")
            beginning = time.time()

        time.sleep(0.1)

    GPIO.cleanup()
