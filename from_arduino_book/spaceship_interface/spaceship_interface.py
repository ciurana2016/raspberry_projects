import time
import RPi.GPIO as GPIO


# Layout
GPIO.setmode(GPIO.BCM)

# Remove warnings
GPIO.setwarnings(False)

# Setup
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Turn off leds
GPIO.output(14, 0) # Red
GPIO.output(15, 0) # Red
GPIO.output(18, 0) # Green

try:
    while True:
        if GPIO.input(23) == 1:
            GPIO.output(14, 1)
            GPIO.output(18, 0)
            time.sleep(.25)
            GPIO.output(14, 0)
            GPIO.output(15, 1)
            time.sleep(.25)
    else:
        GPIO.output(14, 0)
        GPIO.output(15, 0)
        GPIO.output(18, 1) # Green
except KeyboardInterrupt:
    GPIO.cleanup()
