import random
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

# counts and assigns tiles' no. of neighboring mines
def set_nums():
    for y in range(size_y):
        for x in range(size_x):
            if get_tile(x, y).mine:
                get_tile(x, y).num = 9
            else:
                for y2 in range(3):
                    for x2 in range(3):
                        if (0 <= y+y2-1 < size_y) and (0 <= x+x2-1 < size_x) and not (y2 == 1 and x2 == 1):
                            if get_tile(x+x2-1, y+y2-1).mine:
                                get_tile(x, y).num += 1

# assigns mines' locations
def lay(x, y):
    m = mines
    tmpx = 0
    tmpy = 0
    while m > 0:
        tmpx = random.randint(0, size_x - 1)
        tmpy = random.randint(0, size_y - 1)
        if not get_tile(tmpx, tmpy).mine and (not tmpy in range(y-1,y+2) or not tmpx in range(x-1,x+2)):
            get_tile(tmpx, tmpy).mine = True
            m -= 1

def domino(x, y):
    '''this function implements the domino effect which is
seen when a tile which doesn't border any mines is picked'''
    global mines
    list = []
    y -= 1
    x -= 1
    for i in range(3):
        for j in range(3):
            if not 0 <= x+j < size_x: continue
            if not 0 <= y+i < size_y: continue
            if get_tile(x+j, y+i).vis: continue
            get_tile(x+j, y+i).vis = True
            if get_tile(x+j, y+i).flag:
                get_tile(x+j, y+i).flag = False
                mines += 1
            if get_tile(x+j, y+i).num == 0:
                list.append([y+i,x+j])
    for i in range(len(list)):
        domino(list[i][1], list[i][0])