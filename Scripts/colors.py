# Imports
import time
import RPi.GPIO as GPIO

answers = {
    # [blue, red, green]
    "red": [0,1,0],
    "blue": [1,0,0],
    "green": [0,0,1],
    "magenta": [1,1,0],
    "yellow": [0,1,1],
    "cyan": [1,0,1],
    "white": [1,1,1]
}

GPIO.setmode(GPIO.BOARD)
ledGreenPin = 35      #define 3 pins of RGBLED
ledRedPin = 33
ledBluePin = 37
GPIO.setup(ledRedPin,GPIO.OUT)      #set 3 pins of RGBLED to output mode
GPIO.setup(ledGreenPin,GPIO.OUT)
GPIO.setup(ledBluePin,GPIO.OUT)
p_Red = GPIO.PWM(ledRedPin,1000)    #configure PMW to 3 pins of RGBLED
p_Red.start(0)
p_Green = GPIO.PWM(ledGreenPin,1000)
p_Green.start(0)
p_Blue = GPIO.PWM(ledBluePin,1000)
p_Blue.start(0)





def turnOff():
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)

def checkAnswer(arrayToCheck,win):
    if answers[win] == arrayToCheck:
        time.sleep(1)
        turnOff()
        print("OK")
        #GPIO.cleanup()
        return "OK"
        exit()
    else:
        time.sleep(1)
        turnOff()
        print("KO")
        #GPIO.cleanup()
        return "KO"
        exit()


def start(win):
    win = win[0]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    right_anwser = win
    if right_anwser == "magenta":
        p_Red.ChangeDutyCycle(0)  #magenta
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(0)
    elif right_anwser == "yellow":
        p_Red.ChangeDutyCycle(0)  #jaune
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(100)
    elif right_anwser == "cyan":
        p_Red.ChangeDutyCycle(100)  #cyan
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(0)
    elif right_anwser == "red":
        p_Red.ChangeDutyCycle(0)  #rouge
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(100)
    elif right_anwser == "blue":
        p_Red.ChangeDutyCycle(100)  #bleu
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(0)
    elif right_anwser == "green":
        p_Red.ChangeDutyCycle(100)  #vert
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(100)
    elif right_anwser == "white":
        p_Red.ChangeDutyCycle(0)  #blanc
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(0)

    # Define buttons
    GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Blue button
    GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Red button
    GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Green button

    # Define LED
    GPIO.setup(36,GPIO.OUT) # Blue LED
    GPIO.setup(38,GPIO.OUT) # Red LED
    GPIO.setup(40,GPIO.OUT) # Green LED

    try:   
        # Infinite loop
        flag = 0
        while True:
            # Get buttons state
            state_blue = GPIO.input(11)
            state_red = GPIO.input(13)
            state_green = GPIO.input(15)
                
            # Check buttons state  
            if state_blue == 1 or state_red == 1 or state_green == 1:
                flag = flag + 1
                time.sleep(0.1)
                if state_blue: GPIO.output(36,GPIO.HIGH)
                if state_red: GPIO.output(38,GPIO.HIGH) 
                if state_green: GPIO.output(40,GPIO.HIGH)
                #print("Blue = ", state_blue)
                #print("Green = ", state_green)
                #print("Red = ", state_red)
                #print("flag = ", flag)
                #print("")
                if flag == 3:
                    return checkAnswer([state_blue, state_red, state_green],win)
            else:
                GPIO.output(36,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
                GPIO.output(40,GPIO.LOW)
        time.sleep(0.1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
