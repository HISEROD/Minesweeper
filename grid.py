from config import *
from tile import *

grid = [[Tile() for j in range(size_x)] for i in range(size_y)]

def get_tile(x, y):
    global grid
    return grid[y][x]

# TODO use these instead of get_tile for everything in Minesweeper.py

def get_mine(x, y):
    return get_tile(x, y).mine
def get_flag(x, y):
    return get_tile(x, y).flag
def get_num(x, y):
    return get_tile(x, y).num
def get_vis(x, y):
    return get_tile(x, y).vis

def mine(x, y):
    get_tile(x, y).mine = True
def make_vis(x, y):
    get_tile(x, y).vis = True
def flag(x, y):
    get_tile(x, y).flag = True
def set_num(x, y, n):
    get_tile(x, y).num = n
