import pygame

a_completer = True

# Prompt a name with [1; 11] characters
def get_name():
    while True:
        name = input("Please enter your name: ")
        if 0 < len(name) < 11:
            return name
        else:
            print("Name must be between 1 and 11 characters.")

# Convert time from seconds to string of minutes and seconds 
def convert_time(t):
	pass

# get the relative position
def get_rel_pos(my_player, W, H, x, y):
	pass

# Drawing each frame of the game
def redraw_window(my_player, players, balls, game_time, 
				  WIN, PLAYER_RADIUS, BALL_RADIUS, 
				  NAME_FONT, TIME_FONT, SCORE_FONT, W, H, map_width, map_height):
	pass
	