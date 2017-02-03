import RPi.GPIO as GPIO
import time


# Layout
GPIO.setmode(GPIO.BCM)

# Remove warning
GPIO.setwarnings(False)

#Setup
gpio_pins = [14, 15, 8, 7]
for i in gpio_pins:
    GPIO.setup(i, GPIO.OUT, initial=0)
    GPIO.output(i, 1)

# Run program
for i in gpio_pins:
    GPIO.output(i, 0)
    time.sleep(.5)
    GPIO.output(i, 1)

# Cleanup
GPIO.cleanup