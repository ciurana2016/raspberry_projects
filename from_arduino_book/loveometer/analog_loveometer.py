'''
    Schematics and original code from this blog:
    http://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
    How to enable SPI
    http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/
'''
import os
import time
import spidev
import RPi.GPIO as GPIO


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# GPIO layout
GPIO.setmode(GPIO.BCM)

# GPIO remove warnings
GPIO.setwarnings(False)

# GPIO setup
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# Turn off leds
GPIO.output(14, 0)
GPIO.output(15, 0)
GPIO.output(18, 0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Function to calculate temperature TMP36
def ConvertTemp(data,places):
    temp = ((data * 330)/float(1023))-50
    temp = round(temp,places)
    return temp

# Check initial temperature
initial_level = ReadChannel(1)
initial_temp = ConvertTemp(initial_level,2)

# Start the "loveometer"
try:
    while True:
        current_level = ReadChannel(1)
        current_temp = ConvertTemp(current_level,2)
        if current_temp < initial_temp:
            GPIO.output(14, 0)
            GPIO.output(15, 0)
            GPIO.output(18, 0)
        elif current_temp >= initial_temp+2 and current_temp < initial_temp+4:
            GPIO.output(14, 1)
            GPIO.output(15, 0)
            GPIO.output(18, 0)
        elif current_temp >= initial_temp+4 and current_temp < initial_temp+6:
            GPIO.output(14, 1)
            GPIO.output(15, 1)
            GPIO.output(18, 0)
        elif current_temp >= initial_temp+6:
            GPIO.output(14, 1)
            GPIO.output(15, 1)
            GPIO.output(18, 1)
        time.sleep(.25)
except KeyboardInterrupt:
    GPIO.cleanup()
