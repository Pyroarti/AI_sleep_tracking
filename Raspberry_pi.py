import socket
import RPi.GPIO as GPIO
import time

RASPBERRY_PI_IP = '192.168.0.124'
RASPBERRY_PI_PORT = 65432

GPIO.setmode(GPIO.BCM)

servo_y_pin = 18
servo_x_pin = 17

GPIO.setup(servo_y_pin, GPIO.OUT)
GPIO.setup(servo_x_pin, GPIO.OUT)

servo_y = GPIO.PWM(servo_y_pin, 50)
servo_x = GPIO.PWM(servo_x_pin, 50)

servo_y.start(0)
servo_x.start(0)

def set_servo_angle(servo, angle):
    """Set the angle of the servo"""
    if angle > 90 or angle < 30:
        print("Invalid angle") # Becuse of how its mounted
        return

    duty = (angle + 90) * (12-2) / 180 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(0.2)


socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.bind((RASPBERRY_PI_IP, RASPBERRY_PI_PORT))
socket_connection.listen()
print(f"Listening on {RASPBERRY_PI_IP}:{RASPBERRY_PI_PORT}")

conn, addr = socket_connection.accept()

try:
    while True:
        data = conn.recv(1024).decode('utf-8')

        if not data:
            print("no data recived")
            break
        print(f"raw data {data}")

        if '\n' in data:
            raw_message = data.strip().split('\n')[-1]
            try:
                servo_x_angle_str, servo_y_angle_str = raw_message.split(",")

                servo_y_angle = float(servo_y_angle_str)
                servo_x_angle = float(servo_x_angle_str)

                print(f"Received angle for servo Y: {servo_y_angle} and for servo x: {servo_x_angle}")

                set_servo_angle(servo_y, servo_y_angle)
                set_servo_angle(servo_x, servo_x_angle)

            except ValueError:
                print("Invalid data received, skipping.")

except KeyboardInterrupt:
    print("Stopping program.")

finally:
    servo_y.stop()
    GPIO.cleanup()
    conn.close()
