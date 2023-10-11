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
		my_player = players[my_id]

		WIN.fill((255,255,255)) # fill screen white
		# draw all the orbs/balls
		for ball in balls:
			pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)

		pygame.draw.circle(WIN, ball[2], (0, 0), BALL_RADIUS)
		# send data to server and recieve back all players information
		returning_values = server.send("move 1 1")
		try:
			if returning_values is not None:
				balls, players, game_time = returning_values
		except:
			print(returning_values)
		pygame.display.update()

		for event in pygame.event.get():
			# if user hits red x button close window
			if event.type == pygame.QUIT:
				run = False


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