import socket
import RPi.GPIO as GPIO
import time


class Servo:
    """
    Class for controlling the servos
    """

    def __init__(self):

        # IO mapping
        servo_x_pin = 17
        servo_y_pin = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_x_pin, GPIO.OUT)
        GPIO.setup(servo_y_pin, GPIO.OUT)

        self.servo_x = GPIO.PWM(servo_x_pin, 50)
        self.servo_y = GPIO.PWM(servo_y_pin, 50)

        self.servo_x.start(0)
        self.servo_y.start(0)

    def set_servo_angle(self, servo, angle):
        """
        Sets the angle of the servo
        """

        if angle > 90 or angle < 30:
            print("Invalid angle")
            return

        duty = (angle + 90) * (12-2) / 180 + 2

        print(duty)
        servo.ChangeDutyCycle(duty)
        time.sleep(1)
        servo.ChangeDutyCycle(0)
        time.sleep(1)


    def stop_servo(self):
        self.servo_x.stop()
        self.servo_y.stop()
        GPIO.cleanup()
        print("Stopped")

class Connection:
    """
    Class for handling the connection to the client and receiving data from pc
    and retreiving the servo data
    """

    def __init__(self):
        self.HOST = '192.168.0.124'  # IP Raspberry Pi
        self.PORT = 65432

        self.conn = None
        self.addr = None
        self.data = None
        self.servo_x_angle = None
        self.servo_y_angle = None

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind((self.HOST, self.PORT))
        connection.listen()
        print(f"Listening on {self.HOST}:{self.PORT}")
        self.conn, self.addr = connection.accept()


    def get_data(self):
        while True:
            self.data = self.conn.recv(1024)
            if not self.data:
                print("no data recived")
                break
        
            self.servo_x_angle, self.servo_y_angle = map(float, self.data.decode('utf-8').split(","))
            print(f"Received angles X: {self.servo_x_angle}, Y: {self.servo_y_angle}")

    def close_connection(self):
        self.conn.close()
        print("Connection closed")


def main():
    servo = Servo()
    connection = Connection()

    try:
        while True:
            connection.get_data()
            if connection.servo_x_angle is not None and connection.servo_y_angle is not None:
                #servo.set_servo_angle(servo.servo_x, connection.servo_x_angle)
                servo.set_servo_angle(servo.servo_y, connection.servo_y_angle)

    except KeyboardInterrupt:
        print("Interrupt received, stopping...")
    except Exception as e:
        print(e)
    finally:
        servo.stop_servo()
        connection.close_connection()

if __name__ == '__main__':
    main()
