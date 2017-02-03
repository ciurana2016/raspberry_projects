import RPi.GPIO as GPIO
import time


# Layout
GPIO.setmode(GPIO.BCM)

# Remove warning
GPIO.setwarnings(False)

#Setup
gpio_pins = [14, 15, 8, 7]
for i,n in enumerate(gpio_pins):
    GPIO.setup(gpio_pins[i], GPIO.OUT, initial=0)
    GPIO.output(gpio_pins[i], 1)

# Run program
for i,n in enumerate(gpio_pins):
    GPIO.output(gpio_pins[i], 0)
    time.sleep(.5)
    GPIO.output(gpio_pins[i], 1)

# Cleanup
GPIO.cleanup