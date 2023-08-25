import socket
import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

servo1 = GPIO.PWM(17, 50) # Pin 17, 50Hz frequency
servo2 = GPIO.PWM(18, 50) # Pin 18, 50Hz frequency

servo1.start(0)
servo2.start(0)

def set_servo_angle(servo, angle):
    if angle > 90 or angle < 30:
        print("Invalid angle")
        return
    duty = (angle + 90) * (12-2) / 180 + 2
    
    print(duty)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    time.sleep(1)

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
#set_servo_angle(servo1, 0)

# Should only move between 30 and 90
set_servo_angle(servo2, 90)

time.sleep(2)

servo1.stop()
servo2.stop()
GPIO.cleanup()
print("Stopped")