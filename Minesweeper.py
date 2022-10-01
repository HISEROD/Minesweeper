import time
import random

grid_x = 16
grid_y = 9

mines = round((grid_x * grid_y -9)/7)

#Store mine locations in list M.
M = []

#Add row lists so that M is a 2D list.
while len(M) < grid_y:
    M.append([])

#Fill each row with 0's.
for i in range(grid_y):
    while len(M[i]) < grid_x:
        M[i].append(0)

#Mine matrix test
def test(a):
    r = ''
    for i in range(len(a)):
        for j in range(len(a[0])):
            r += str(a[i][j]) + ' '
        print(r)
        r = ''

#Create indicator matrix.
I = []

#Add row lists.
while len(I) < grid_y:
    I.append([])

#Fill each column with 0's.
for i in range(grid_y):
    while len(I[i]) < grid_x:
        I[i].append(0)

#Assign number of bordering mines to each square.

#Create a search adjacent function since this functionality is used often.
def search():
    for y in range(grid_y):
        for x in range(grid_x):
            if M[y][x] == 1:
                I[y][x] = 9
            else:
                for i in range(3):
                    for j in range(3):
                        if (0 <= y+i-1 < grid_y) and (0 <= x+j-1 < grid_x) and not (i == 1 and j == 1):
                            if M[y+i-1][x+j-1] == 1:
                                I[y][x] += 1


#Indicator matrix test
def testI():
    for i in range(len(I)):
        print(I[i])

#Create flag matrix.
F = []

#Add row lists.
while len(F) < grid_y:
    F.append([])

#Fill each column with 0's.
for i in range(grid_y):
    while len(F[i]) < grid_x:
        F[i].append(0)

#Create visibility matrix.
V = []

#Add row lists.
while len(V) < grid_y:
    V.append([])

#Fill each column with 0's.
for i in range(grid_y):
    while len(V[i]) < grid_x:
        V[i].append(0)


#Assign mines' locations as 1's.
def lay():
    m = mines
    tmpx = 0
    tmpy = 0
    while m > 0:
        tmpx = random.randint(0, grid_x - 1)
        tmpy = random.randint(0, grid_y - 1)
        if M[tmpy][tmpx] == 0 and (not tmpy in range(y-1,y+2) or not tmpx in range(x-1,x+2)):
            M[tmpy][tmpx] = 1
            m -= 1


"""

-------TIME TO DRAW-------

"""

def youWin():
    print("")
    print("▓▓    ▓▓   ▓▓▓▓▓   ▓▓   ▓▓")
    print(" ▓▓  ▓▓   ▓▓   ▓▓  ▓▓   ▓▓")
    print("  ▓▓▓▓    ▓▓   ▓▓  ▓▓   ▓▓")
    print("   ▓▓     ▓▓   ▓▓  ▓▓   ▓▓")
    print("   ▓▓     ▓▓   ▓▓  ▓▓   ▓▓")
    print("   ▓▓      ▓▓▓▓▓    ▓▓▓▓▓")
    print("")
    print("▓▓      ▓▓  ▓▓  ▓▓   ▓▓ ▓▓")
    print("▓▓      ▓▓  ▓▓  ▓▓▓  ▓▓ ▓▓")
    print("▓▓  ▓▓  ▓▓  ▓▓  ▓▓▓▓ ▓▓ ▓▓")
    print("▓▓ ▓▓▓▓ ▓▓  ▓▓  ▓▓ ▓▓▓▓ ▓▓")
    print(" ▓▓▓  ▓▓▓   ▓▓  ▓▓  ▓▓▓")
    print(" ▓▓    ▓▓   ▓▓  ▓▓   ▓▓ ▓▓")
    print("")

def domino(y,x):
    global mines
    list = []
    y -= 1
    x -= 1
    for i in range(3):
        for j in range(3):
            if (0 <= y+i < grid_y) and (0 <= x+j < grid_x) and (V[y+i][x+j] == 0):
                V[y+i][x+j] = 1
                if F[y+i][x+j]:
                    F[y+i][x+j] = 0
                    mines += 1
                if I[y+i][x+j] == 0:
                    list.append([y+i,x+j])
    for i in range(len(list)):
        domino(list[i][0],list[i][1])

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
topsc = ' ' * len(str(grid_y))

for i in range(grid_x):
    topsc += ' ' + alph[i]

row = ''

def checkWinLose():
    x = 1
    for i in range(grid_y):
        for j in range(grid_x):
            if not V[i][j] and not M[i][j]:
                x = 0
            elif V[i][j] and M[i][j]:
                x = -1
                break
        if x == -1:
            break
    return x

x,y = 0,0

# time

start_time = time.time()

def seconds():
    return str(round(time.time() - start_time))

#initial info and grid
print('Time: 0     Flags: ' + str(mines))
print(topsc)
for i in range(grid_y):
    for j in range(grid_x):
            row += ' ' + '|'
    row = (len(str(grid_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#first move
strin = input()
x = alph.index(strin[0])
y = int(strin[1:])-1
V[y][x] = 1
lay()
search()
if I[y][x] == 0:
    domino(y,x)

print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
print(topsc)
for i in range(grid_y):
    for j in range(grid_x):
        if V[i][j] == 1:
            if I[i][j] > 0:
                if I[i][j] == 9:
                    row += 'X' + '|'
                else:
                    row += str(I[i][j]) + '|'
            else:
                row += '░' + '|'
        elif F[i][j] == 1:
            row += '■' + '|'
        else:
            row += ' ' + '|'
    row = (len(str(grid_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
    print(row)
    row = ''

#Loop until win or lose.
while True:
    strin = input()
    x = alph.index(strin[1])
    y = int(strin[2:])-1
    if strin[0] == 'f' and F[y][x] == 0:
        F[y][x] = 1
        mines -= 1
    elif strin[0] == 'r' and F[y][x] == 1:
        F[y][x] = 0
        mines += 1
    elif strin[0] == 'd' and V[y][x] == 0:
        V[y][x] = 1
        if I[y][x] == 0:
            domino(y,x)
    if checkWinLose() == -1:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(topsc)
        for i in range(grid_y):
            for j in range(grid_x):
                if V[i][j] == 1:
                    if I[i][j]:
                        if I[i][j] == 9:
                            row += '‼' + '|'
                        else:
                            row += str(I[i][j]) + '|'
                    else:
                        row += '░' + '|'
                elif F[i][j] and not M[i][j]:
                    row += '■' + '|'
                elif F[i][j] and M[i][j]:
                    row += 'X' + '|'
                elif M[i][j]:
                    row += '‼' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(grid_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
            print(row)
            row = ''
        break
    else:
        print('Time: ' + seconds() + (6 - len(seconds())) * ' ' + 'Flags: ' + str(mines))
        print(topsc)
        for i in range(grid_y):
            for j in range(grid_x):
                if V[i][j] == 1:
                    if I[i][j] > 0:
                        row += str(I[i][j]) + '|'
                    else:
                        row += '░' + '|'
                elif F[i][j] == 1:
                    row += '■' + '|'
                else:
                    row += ' ' + '|'
            row = (len(str(grid_y)) - len(str(i + 1))) * ' '  + str(i + 1) + '|' + row
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
