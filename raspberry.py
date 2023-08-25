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
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    servo.ChangeDutyCycle(0)

HOST = '192.168.0.124'  # Local IP Address of Raspberry Pi
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("no data recived")
                    break
            
                servo_x_angle, servo_y_angle = map(float, data.decode('utf-8').split(","))
                print(f"Received angles X: {servo_x_angle}, Y: {servo_y_angle}")

            #set_servo_angle(servo1, servo_x_angle)
            #set_servo_angle(servo2, servo_y_angle)




