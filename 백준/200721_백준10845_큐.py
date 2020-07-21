import sys
import operator as op


# 명령의 수
N = int(input())


# 큐 리스트 정의
queue = []


# 결과 리스트 정의
result = []

def push(X):
    queue.append(X)

def pop():
    if not queue:
        return result.append(-1)   
    else:
        result.append(queue[0]) 
        del queue[0]
        return 

def size():
    return result.append(len(queue))
    

def empty():
    if not queue:
        return result.append(1)
    else:
        return result.append(0)

def front():
    if not queue:
        return result.append(-1)
    else:
        return result.append(queue[0])
        

def back():
    if not queue:
        return result.append(-1)
    else:
        return result.append(queue[-1])
    



for i in range(N):
    Input_Command = list(sys.stdin.readline().split())
    
    if len(Input_Command) == 2:
        Input_X = int(Input_Command[1])
        push(Input_X)
    elif Input_Command[0] == "pop":
        pop()
    elif Input_Command[0] == "size":
        size()
    elif Input_Command[0] == "empty":
        empty()
    elif Input_Command[0] == "front":
        front()
    elif Input_Command[0] == "back":
        back()


for i in range(len(result)):
    print(result[i])
