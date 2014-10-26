import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '172.16.0.2'
port = 8883
print('Connecting with server...')
s.connect((host, port))
print('Connected')
print(s.recv(1024))
usr = input()
s.send(str(usr))
print(s.recv(1024))
psswrd = input()
s.send(str(psswrd))
while True:
	
		
	import pygame
	WHITE = [23, 67, 99]
	pygame.init()
	 
	size = [500, 700]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Sub")

	done = False


	clock = pygame.time.Clock()


	pygame.joystick.init()
	joystick = pygame.joystick.Joystick(0)
	joystick.init()



	while done==False:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT: 
	            done=True 

	    screen.fill(WHITE)


	   
	    axis_one_value = joystick.get_axis(0)
	    axis_two_value = joystick.get_axis(1)

	    s.send(str(axis_two_value))
	    ##s.send(str(axis_one_value))


	    pygame.display.flip()

	 
	    clock.tick(20)
	    

	pygame.quit ()
	sys.exit()

	