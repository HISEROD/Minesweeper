import time
import random
from string import ascii_lowercase

# set config values
GRID_X = 14
GRID_Y = 8
DENSITY = 1 / 5 # 20% chance of mine

# set the number of mines based on the # of
# available tiles times the density factor
mines = round(GRID_X * GRID_Y * DENSITY)

#Store mine locations in mine_matrix.
mine_matrix = []

#Add row lists so that mine_matrix is a 2D list.
while len(mine_matrix) < GRID_Y:
    mine_matrix.append([])

#Fill each row with 0's.
for i in range(GRID_Y):
    while len(mine_matrix[i]) < GRID_X:
        mine_matrix[i].append(0)

#Mine matrix test
def test(a):
    r = ''
    for i in range(len(a)):
        for j in range(len(a[0])):
            r += str(a[i][j]) + ' '
        print(r)
        r = ''

#Create indicator matrix.
indicator_matrix = []

#Add row lists.
while len(indicator_matrix) < GRID_Y:
    indicator_matrix.append([])

#Fill each column with 0's.
for i in range(GRID_Y):
    while len(indicator_matrix[i]) < GRID_X:
        indicator_matrix[i].append(0)

#Assign number of bordering mines to each square.

#Create a search adjacent function since this functionality is used often.
def search():
    for y in range(GRID_Y):
        for x in range(GRID_X):
            if mine_matrix[y][x] == 1:
                indicator_matrix[y][x] = 9
            else:
                for i in range(3):
                    for j in range(3):
                        if (0 <= y+i-1 < GRID_Y) and (0 <= x+j-1 < GRID_X) and not (i == 1 and j == 1):
                            if mine_matrix[y+i-1][x+j-1] == 1:
                                indicator_matrix[y][x] += 1


#Indicator matrix test
def testI():
    for i in range(len(indicator_matrix)):
        print(indicator_matrix[i])

#Create flag matrix.
flag_matrix = []

#Add row lists.
while len(flag_matrix) < GRID_Y:
    flag_matrix.append([])

#Fill each column with 0's.
for i in range(GRID_Y):
    while len(flag_matrix[i]) < GRID_X:
        flag_matrix[i].append(0)

#Create visibility matrix.
visibility_matrix = []

#Add row lists.
while len(visibility_matrix) < GRID_Y:
    visibility_matrix.append([])

#Fill each column with 0's.
for i in range(GRID_Y):
    while len(visibility_matrix[i]) < GRID_X:
        visibility_matrix[i].append(0)


#Assign mines' locations as 1's.
def lay():
    m = mines
    tmpx = 0
    tmpy = 0
    while m > 0:
        tmpx = random.randint(0, GRID_X - 1)
        tmpy = random.randint(0, GRID_Y - 1)
        if mine_matrix[tmpy][tmpx] == 0 and (not tmpy in range(y-1,y+2) or not tmpx in range(x-1,x+2)):
            mine_matrix[tmpy][tmpx] = 1
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
            if (0 <= y+i < GRID_Y) and (0 <= x+j < GRID_X) and (visibility_matrix[y+i][x+j] == 0):
                visibility_matrix[y+i][x+j] = 1
                if flag_matrix[y+i][x+j]:
                    flag_matrix[y+i][x+j] = 0
                    mines += 1
                if indicator_matrix[y+i][x+j] == 0:
                    list.append([y+i,x+j])
    for i in range(len(list)):
        domino(list[i][0],list[i][1])

letters = ascii_lowercase
topsc = ' ' * len(str(GRID_Y))

for i in range(GRID_X):
    topsc += ' ' + letters[i]

row = ''

def checkWinLose():
    '''Returns 1 for a win, -1 for a loss, or 0 for neither.'''
    indicator = 1 # default to win
    for y in range(GRID_Y):
        for x in range(GRID_X):
            if not visibility_matrix[y][x] and not mine_matrix[y][x]:
                indicator = 0 # if a tile is
            elif visibility_matrix[y][x] and mine_matrix[y][x]:
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
print(topsc)
for i in range(GRID_Y):
    for j in range(GRID_X):
            row += ' ' + '|'
    row = (len(str(GRID_Y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#first move
strin = input()
x = letters.index(strin[0])
y = int(strin[1:])-1
visibility_matrix[y][x] = 1
lay()
search()
if indicator_matrix[y][x] == 0:
    domino(y,x)

print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
print(topsc)
for i in range(GRID_Y):
    for j in range(GRID_X):
        if visibility_matrix[i][j] == 1:
            if indicator_matrix[i][j] > 0:
                if indicator_matrix[i][j] == 9:
                    row += 'X' + '|'
                else:
                    row += str(indicator_matrix[i][j]) + '|'
            else:
                row += '░' + '|'
        elif flag_matrix[i][j] == 1:
            row += '■' + '|'
        else:
            row += ' ' + '|'
    row = (len(str(GRID_Y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#Loop until win or lose.
while True:
    strin = input()
    x = letters.index(strin[1])
    y = int(strin[2:])-1
    if strin[0] == 'f' and flag_matrix[y][x] == 0:
        flag_matrix[y][x] = 1
        mines -= 1
    elif strin[0] == 'r' and flag_matrix[y][x] == 1:
        flag_matrix[y][x] = 0
        mines += 1
    elif strin[0] == 'd' and visibility_matrix[y][x] == 0:
        visibility_matrix[y][x] = 1
        if indicator_matrix[y][x] == 0:
            domino(y,x)
    if checkWinLose() == -1:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(topsc)
        for i in range(GRID_Y):
            for j in range(GRID_X):
                if visibility_matrix[i][j] == 1:
                    if indicator_matrix[i][j]:
                        if indicator_matrix[i][j] == 9:
                            row += '‼' + '|'
                        else:
                            row += str(indicator_matrix[i][j]) + '|'
                    else:
                        row += '░' + '|'
                elif flag_matrix[i][j] and not mine_matrix[i][j]:
                    row += '■' + '|'
                elif flag_matrix[i][j] and mine_matrix[i][j]:
                    row += 'X' + '|'
                elif mine_matrix[i][j]:
                    row += '‼' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(GRID_Y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
            print(row)
            row = ''
        break
    else:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(topsc)
        for i in range(GRID_Y):
            for j in range(GRID_X):
                if visibility_matrix[i][j] == 1:
                    if indicator_matrix[i][j] > 0:
                        row += str(indicator_matrix[i][j]) + '|'
                    else:
                        row += '░' + '|'
                elif flag_matrix[i][j] == 1:
                    row += '■' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(GRID_Y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
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
