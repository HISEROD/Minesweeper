import time
from string import ascii_lowercase as letters

from config import *
from grid import *

top_scale = ' ' * len(str(size_y))

for i in range(size_x):
    top_scale += ' ' + letters[i]

row = ''

def check_win_lose():
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

# initial info and grid
print('Time: 0     Flags: ' + str(flags))
print(top_scale)
for i in range(size_y):
    for j in range(size_x):
            row += ' ' + '|'
    row = (len(str(size_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

# first move
strin = input()
x = letters.index(strin[0])
y = int(strin[1:])-1
get_tile(x, y).vis = True
lay(x, y)
set_nums()
if get_tile(x, y).num == 0:
    domino(x, y)

print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(flags))
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

# loop until win or lose
while True:
    strin = input()
    x = letters.index(strin[1])
    y = int(strin[2:])-1
    if strin[0] == 'f' and not get_tile(x, y).flag:
        get_tile(x, y).flag = 1
        flags -= 1
    elif strin[0] == 'r' and get_tile(x, y).flag:
        get_tile(x, y).flag = 0
        flags += 1
    elif strin[0] == 'd' and not get_tile(x, y).vis:
        get_tile(x, y).vis = True
        if get_tile(x, y).num == 0:
            domino(x, y)
    if check_win_lose() == -1:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(flags))
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
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(flags))
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
    if check_win_lose() == 1:
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
        break

if check_win_lose() == -1:
    print('You got blown up by a mine!')
    time.sleep(1)
    input('Press Enter to leave.')
else:
    time.sleep(2)
    input('Press Enter to leave.')
