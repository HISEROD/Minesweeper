# define grid size
size_x = 14
size_y = 8

# 20% chance of mine
_density = 1 / 5

# set the number of mines based on the # of
# available tiles times the density factor
mines = round(size_x * size_y * _density)
flags = mines