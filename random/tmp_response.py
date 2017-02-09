import time
import commands
import RPi.GPIO as GPIO


# Layout
GPIO.setmode(GPIO.BCM)

# Remove warnings
GPIO.setwarnings(False)

# Setup
GPIO.setup(17, GPIO.OUT)
servo = GPIO.PWM(17, 50)
servo.start(12.5)

# Our program 
try:
    tmp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp')
    tmp = flaot(tmp[5:][:-2])
    if tmp > 42.0:
        servo.ChangeDutyCycle(15.5) # Servo down
        time.sleep(2)
        servo.stop()
        time.sleep(60 * 9) # 9 min
        servo.ChangeDutyCycle(.5) # Servo up
        time.sleep(1.5)
        servo.stop()

except KeyboardInterrup:
	pass

# Reset servo
servo.ChangeDutyCycle(.5)
time.sleep(1.5)
servo.stop()
GPIO.cleanup()
