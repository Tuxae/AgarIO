import pygame
from client import Network
import os

from function import *
from constant import *



def main(name):
	# start by connecting to the network
	server = Network()
	my_id = server.connect(name)
	balls, players, game_time = server.send("get")

	# setup the clock
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(30) # sync to 30fps
		my_player = a_completer

		# get MOUSE position
		mouse_pos = pygame.a_completer.get_pos()
		
		#movement based on mouse position
		dx = mouse_pos[0] - W/2
		dy = mouse_pos[1] - a_completer
		data = f"move " + str(dx) + " " + str(a_completer)
		
		# SEND data to server and recieve back all players information
		returning_values = server.a_completer(data)
		try:
			if returning_values is not None:
				balls, players, game_time = a_completer
		except:
			print(returning_values)

		for event in pygame.event.get():
			# if user hits red x button close window
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				# if user hits a escape key close program
				run = False


		# redraw window then update the frame
		redraw_window(a_completer)
		pygame.display.update()


	server.disconnect()
	pygame.quit()
	quit()

# get users name
name = get_name()

# setup pygame window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption("TUXAE")

# start game
main(name)