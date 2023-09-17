import socket
import time

HOST = '192.168.0.124'  # The IP address of your Raspberry Pi
PORT = 65432  # The port you defined in the Raspberry Pi code

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Raspberry Pi
s.connect((HOST, PORT))

try:
    while True:
        # Replace 30.0 and 70.0 with the angles you want to send for X and Y
        s.sendall(b'30.0,30.0\n')
        time.sleep(1)
        s.sendall(b'30.0,40.0\n')
        time.sleep(1)
        s.sendall(b'30.0,50.0\n')
        time.sleep(1)
        s.sendall(b'30.0,60.0\n')
        time.sleep(1)
        s.sendall(b'30.0,70.0\n')
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping client.")
finally:
    s.close()
