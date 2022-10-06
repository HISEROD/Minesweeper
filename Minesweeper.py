import time
import random
from string import ascii_lowercase

from config import *
from grid import *

#Assign number of bordering mines to each square.

#Create a search adjacent function since this functionality is used often.
def search():
    for y in range(size_y):
        for x in range(size_x):
            if get_tile(x, y).mine:
                get_tile(x, y).num = 9
            else:
                for i in range(3):
                    for j in range(3):
                        if (0 <= y+i-1 < size_y) and (0 <= x+j-1 < size_x) and not (i == 1 and j == 1):
                            if get_tile(x+j-1, y+i-1).mine:
                                get_tile(x, y).num += 1


#Assign mines' locations as 1's.
def lay():
    m = mines
    tmpx = 0
    tmpy = 0
    while m > 0:
        tmpx = random.randint(0, size_x - 1)
        tmpy = random.randint(0, size_y - 1)
        if not get_tile(tmpx, tmpy).mine and (not tmpy in range(y-1,y+2) or not tmpx in range(x-1,x+2)):
            get_tile(tmpx, tmpy).mine = True
            m -= 1


'''

-------TIME TO DRAW-------

'''

def youWin():
    print('''
▓▓    ▓▓   ▓▓▓▓▓   ▓▓   ▓▓
 ▓▓  ▓▓   ▓▓   ▓▓  ▓▓   ▓▓
  ▓▓▓▓    ▓▓   ▓▓  ▓▓   ▓▓
   ▓▓     ▓▓   ▓▓  ▓▓   ▓▓
   ▓▓     ▓▓   ▓▓  ▓▓   ▓▓
   ▓▓      ▓▓▓▓▓    ▓▓▓▓▓

▓▓      ▓▓  ▓▓  ▓▓   ▓▓ ▓▓
▓▓      ▓▓  ▓▓  ▓▓▓  ▓▓ ▓▓
▓▓  ▓▓  ▓▓  ▓▓  ▓▓▓▓ ▓▓ ▓▓
▓▓ ▓▓▓▓ ▓▓  ▓▓  ▓▓ ▓▓▓▓ ▓▓
 ▓▓▓  ▓▓▓   ▓▓  ▓▓  ▓▓▓
 ▓▓    ▓▓   ▓▓  ▓▓   ▓▓ ▓▓
''')

def domino(y,x):
    '''this function implements the domino effect which is
seen when a tile which doesn't border any mines is selected'''
    global mines
    list = []
    y -= 1
    x -= 1
    for i in range(3):
        for j in range(3):
            if (0 <= y+i < size_y) and (0 <= x+j < size_x) and not get_tile(x+j, y+i).vis:
                get_tile(x+j, y+i).vis = True
                if get_tile(x+j, y+i).flag:
                    get_tile(x+j, y+i).flag = False
                    mines += 1
                if get_tile(x+j, y+i).num == 0:
                    list.append([y+i,x+j])
    for i in range(len(list)):
        domino(list[i][0],list[i][1])

letters = ascii_lowercase
top_scale = ' ' * len(str(size_y))

for i in range(size_x):
    top_scale += ' ' + letters[i]

row = ''

def checkWinLose():
    '''Returns 1 for a win, -1 for a loss, or 0 for neither.'''
    indicator = 1 # default to win
    for y in range(size_y):
        for x in range(size_x):
            if not get_tile(x, y).vis and not get_tile(x, y).mine:
                indicator = 0 # if a tile is
            elif get_tile(x, y).vis and get_tile(x, y).mine:
                indicator = -1
                break
        if indicator == -1:
            break
    return indicator

x,y = 0,0

# time

start_time = time.time()

def seconds():
    return str(round(time.time() - start_time))

#initial info and grid
print('Time: 0     Flags: ' + str(mines))
print(top_scale)
for i in range(size_y):
    for j in range(size_x):
            row += ' ' + '|'
    row = (len(str(size_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#first move
strin = input()
x = letters.index(strin[0])
y = int(strin[1:])-1
get_tile(x, y).vis = True
lay()
search()
if get_tile(x, y).num == 0:
    domino(y,x)

print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
print(top_scale)
for i in range(size_y):
    for j in range(size_x):
        if get_tile(j, i).vis:
            if get_tile(j, i).num > 0:
                if get_tile(j, i).num == 9:
                    row += 'X' + '|'
                else:
                    row += str(get_tile(j, i).num) + '|'
            else:
                row += '░' + '|'
        elif get_tile(j, i).flag:
            row += '■' + '|'
        else:
            row += ' ' + '|'
    row = (len(str(size_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#Loop until win or lose.
while True:
    strin = input()
    x = letters.index(strin[1])
    y = int(strin[2:])-1
    if strin[0] == 'f' and not get_tile(x, y).flag:
        get_tile(x, y).flag = 1
        mines -= 1
    elif strin[0] == 'r' and get_tile(x, y).flag:
        get_tile(x, y).flag = 0
        mines += 1
    elif strin[0] == 'd' and not get_tile(x, y).vis:
        get_tile(x, y).vis = True
        if get_tile(x, y).num == 0:
            domino(y,x)
    if checkWinLose() == -1:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(top_scale)
        for i in range(size_y):
            for j in range(size_x):
                if get_tile(j, i).vis:
                    if get_tile(j, i).num:
                        if get_tile(j, i).num == 9:
                            row += '‼' + '|'
                        else:
                            row += str(get_tile(j, i).num) + '|'
                    else:
                        row += '░' + '|'
                elif get_tile(j, i).flag and not get_tile(j, i).mine:
                    row += '■' + '|'
                elif get_tile(j, i).flag and get_tile(j, i).mine:
                    row += 'X' + '|'
                elif get_tile(j, i).mine:
                    row += '‼' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(size_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
            print(row)
            row = ''
        break
    else:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(top_scale)
        for i in range(size_y):
            for j in range(size_x):
                if get_tile(j, i).vis:
                    if get_tile(j, i).num > 0:
                        row += str(get_tile(j, i).num) + '|'
                    else:
                        row += '░' + '|'
                elif get_tile(j, i).flag:
                    row += '■' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(size_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
            print(row)
            row = ''
    if checkWinLose() == 1:
        youWin()
        break

if checkWinLose() == -1:
    print('You got blown up by a mine!')
    time.sleep(1)
    input('Press Enter to leave.')
else:
    time.sleep(2)
    input('Press Enter to leave.')
