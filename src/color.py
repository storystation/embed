# Imports
import time
import RPi.GPIO as GPIO


def start(win):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # Define buttons
    GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Blue button
    GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Red button
    GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Green button

    # Define LED
    GPIO.setup(36,GPIO.OUT) # Blue LED
    GPIO.setup(38,GPIO.OUT) # Red LED
    GPIO.setup(40,GPIO.OUT) # Green LED

    right_anwser = win

    answers = {
        # [blue, red, green]
        "red": [0,1,0],
        "blue": [1,0,0],
        "green": [0,0,1],
        "mangeta": [1,1,0],
        "yellow": [0,1,1],
        "cyan": [1,0,1],
        "white": [1,1,1]
    }


    def checkAnswer(arrayToCheck):
        if answers[rightAnswer] == arrayToCheck:
            return "OK"
        else:
            return "KO"

    # Infinite loop
    while True:
        # Get buttons state
        state_blue = GPIO.input(11)
        state_red = GPIO.input(13)
        state_green = GPIO.input(15)
        
        
        # Check buttons state
        if state_blue == 1 or state_red == 1 or state_green == 1:
            time.sleep(0.1)
            if state_blue: GPIO.output(36,GPIO.HIGH)
            if state_blue: GPIO.output(38,GPIO.HIGH) 
            if state_blue: GPIO.output(40,GPIO.HIGH) 

            checkAnswer([state_blue, state_red, state_green])

        time.sleep(0.1)
