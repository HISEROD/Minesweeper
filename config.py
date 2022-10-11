# define grid size
size_x = 8
size_y = 8

# 20% chance of mine
_density = 1 / 6

# set the number of mines based on the # of
# available tiles times the density factor
flags = round(size_x * size_y * _density)

'''this var is called flags because after
laying the mines (see "lay" function in grid.py),
it is used exclusively for tracking the number of
flags as an aid esp. at the end of the game'''
