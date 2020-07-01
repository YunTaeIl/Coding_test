import sys
import operator as op
from functools import reduce


def transX(num):
    if num == 'A':
        return 0
    elif num == 'B':
        return 1
    elif num == 'C':
        return 2
    elif num == 'D':
        return 3
    elif num == 'E':
        return 4
    elif num == 'F':
        return 5
    elif num == 'G':
        return 6
    elif num == 'H':
        return 7

def transY(num):
    return int(num) - 1

def rev_transX(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'B'
    elif num == 2:
        return 'C'
    elif num == 3:
        return 'D'
    elif num == 4:
        return 'E'
    elif num == 5:
        return 'F'
    elif num == 6:
        return 'G'
    elif num == 7:
        return 'H'

def rev_transY(num):
    return int(num) + 1


def movePoint(dir):
    if dir == 'R':
        return 1, 0
    elif dir == 'L':
        return -1, 0
    elif dir == 'B':
        return 0,-1
    elif dir == 'T':
        return 0, 1
    elif dir == 'RT':
        return 1, 1
    elif dir == 'LT':
        return -1, 1
    elif dir == 'RB':
        return 1, -1
    elif dir == 'LB':
        return -1, -1
    else: return 0,0

# 현재 킹과 돌의 위치 반환
def locationK():
    for i in range(8):
        for j in range(8):
            if Chess_Board[i][j] == 1:
                return i, j

def locationS():
    for i in range(8):
        for j in range(8):
            if Chess_Board[i][j] == 2:
                return i, j
            

# 체스판
Chess_Board = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]


K, S, N = sys.stdin.readline().split()

# 킹의 최초 x좌표 y좌표
x_K = transX(list(K)[0])
y_K = transY(list(K)[1])

# 돌의 최초 x좌표 y좌표
x_S = transX(list(S)[0])
y_S = transY(list(S)[1])

# 킹의 위치는 +1
Chess_Board[x_K][y_K] += 1

# 돌의 위치는 +2
Chess_Board[x_S][y_S] += 2

# 여기에 for문

for _ in range(int(N)):
    # 왕의 현재 위치
    new_x_K, new_y_K = locationK() 
    # 돌의 현재 위치
    new_x_S, new_y_S = locationS() 

    # 움직일 방향
    #X, Y = movePoint(sys.stdin.read())
    X, Y = movePoint(input())

    #X, Y = movePoint(aa)

    #print(X, Y)

    #킹부터 움직임
    if new_x_K + X > 7 or new_x_K + X < 0 or new_y_K + Y > 7 or new_y_K + Y < 0 : 
        continue
    else :
        if new_x_K + X == new_x_S and new_y_K + Y == new_y_S:
            if new_x_S + X > 7 or new_x_S + X < 0 or new_y_S + Y > 7 or new_y_S + Y < 0:
                continue
            else :
                Chess_Board[new_x_S][new_y_S] -= 2
                new_x_S += X
                new_y_S += Y
                Chess_Board[new_x_S][new_y_S] += 2

        Chess_Board[new_x_K][new_y_K] -= 1
        new_x_K += X
        new_y_K += Y
        Chess_Board[new_x_K][new_y_K] += 1

result1, result2 = locationK()
result3, result4 = locationS()

print(rev_transX(result1)+str(rev_transY(result2)))
print(rev_transX(result3)+str(rev_transY(result4)))
