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
	a_completer

# get the relative position
def get_rel_pos(my_player, W, H, x, y):
	x_rel = x-my_player["x"] + W/2
	y_rel = y-my_player["y"] + H/2
	return (x_rel, y_rel)

# Drawing each frame of the game
def redraw_window(my_player, players, balls, game_time, 
				  WIN, PLAYER_RADIUS, BALL_RADIUS, 
				  NAME_FONT, TIME_FONT, SCORE_FONT, W, H, map_width, map_height):
	
	WIN.fill((255,255,255)) # fill screen white

	# draw limit
	pygame.draw.rect(WIN, (251, 244, 226), get_rel_pos(my_player, W, H, 0, 0)+(map_width, map_height), 1000)

    # draw all the orbs/balls
	for ball in balls:
		a_completer # pygame.draw.circle

	# draw each player in the list
	for player in sorted(players, key=lambda x: players[x]["score"]):
		p = a_completer
		a_completer # pygame.draw.circle 
		# render and draw name for each player
		text = NAME_FONT.render(p["name"], 1, (200, 200, 200))
		WIN.blit(text, get_rel_pos(my_player, W, H, p["x"]-text.get_width()/2, p["y"]-text.get_height()/2))

	# draw scoreboard
	sort_players = list(reversed(sorted(players, key=lambda x: players[x]["score"])))
	title = TIME_FONT.render("Scoreboard", 1, (0,0,0))
	x = W - title.get_width() - 15
	WIN.blit(title, (x, 5))

	top10 = min(len(players), 10)
	for count, i in enumerate(sort_players[:top10]):
		text = SCORE_FONT.render(str(count+1) + ". " + str(players[i]["name"]), 1, (0,0,0))
		WIN.blit(text, (x, 35 + count * 25))

	# draw time
	text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (0,0,0))
	WIN.blit(text,(10,10))
	
	# draw score
	text = TIME_FONT.render("Score: " + str(round(my_player["score"])),1,(0,0,0))
	WIN.blit(text,(10,15 + text.get_height()))
	