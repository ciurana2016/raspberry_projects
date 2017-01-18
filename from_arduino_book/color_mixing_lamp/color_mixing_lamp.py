'''
    Schematics and original code from this blog:
    http://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
    How to enable SPI:
    http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/
    You also need to know how to dim a led:
    https://www.youtube.com/watch?v=uUn0KWwwkq8
'''
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

g1 = GPIO.PWM(14, 50)
g2 = GPIO.PWM(15, 50)
g3 = GPIO.PWM(18, 50)

g1.start(0)
g2.start(0)
g3.start(0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Start the "lamp"
try:
    while True:
        rc1 = ReadChannel(5)
        rc2 = ReadChannel(6)
        rc3 = ReadChannel(7)
        rc1 = (rc1-100)/10 if (rc1-100)/10 > 0 else 0
        rc2 = (rc2-100)/10 if (rc2-100)/10 > 0 else 0
        rc3 = (rc3-100)/10 if (rc3-100)/10 > 0 else 0
        g1.ChangeDutyCycle(rc1)
        g2.ChangeDutyCycle(rc2)
        g3.ChangeDutyCycle(rc3)
        time.sleep(.02)
except KeyboardInterrupt:
    pass

g1.stop()
g2.stop()
g3.stop()
GPIO.cleanup()

