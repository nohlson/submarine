import socket
import sys
import time

from Adafruit_PWM_Servo_Driver import PWM
motor = 0x40

pwm = PWM(motor, debug=True)
pwm.setPWMFreq(60)




HOST = ''
PORT = 8883

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
try:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST, PORT))
except socket.error:
	print("Failed to bind host and port.")
	s.close()
	sys.exit()

print("Server established waiting for controller client connection...")

s.listen(1)
conn, addr = s.accept()

def main():
	while 1:
		incomingControl = float(conn.recv(1024))
		value1 = (incomingControl * 4000) - 3
		value2 = abs(int(value1))
		print(value2)
		pwm.setPWM(0, 0, value2)
		

def startup():
	while 1:
		

		print("Connected with " + addr[0] + ":" + str(addr[1]))
		conn.send("Welcome to the sub control center. Enter your username:")
		data = conn.recv(1024)
		if int(data) == 17:
			conn.sendall("Enter password:")
			password = conn.recv(1024)
			if int(password) == 44:
				conn.sendall("Login successfull")

				main()
			elif not password:
				break
		elif not data:
			break
		else:
			pass
		if int(data) == 69:
			sys.exit()

	conn.close()
	s.close()
startup()

