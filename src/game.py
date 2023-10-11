import pygame
from client import Network
import os

from function import *
from constant import *



def main(name):
	# start by connecting to the network
	server = Network()
	my_id = server.connect(name)

	ok= False
	while not ok:
		try:
			balls, players, game_time = server.send("get")
			ok=True
		except:
			pass

	# setup the clock
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(30) # sync to 30fps
		my_player = players[my_id]

		# get mouse position
		mouse_pos = pygame.mouse.get_pos()
		
		#movement based on mouse position
		dx = mouse_pos[0] - W/2
		dy = mouse_pos[1] - H/2
		data = f"move " + str(dx) + " " + str(dy)
		
		# send data to server and recieve back all players information
		returning_values = server.send(data)
		try:
			if returning_values is not None:
				balls, players, game_time = returning_values
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
		redraw_window(my_player, players, balls, game_time, 
				WIN, PLAYER_RADIUS, BALL_RADIUS, 
				NAME_FONT, TIME_FONT, SCORE_FONT, W, H, 
				map_width, map_height
		)
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