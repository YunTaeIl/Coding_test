import sys
import operator as op

# 명령의 수
N = int(input())

# 명령어
Command = ""


# 스택 리스트 정의
stack = []


# 결과 리스트 정의
result = []

def push(X):
    stack.append(X)

def pop():
    if len(stack) != 0:
        
        return result.append(stack.pop())
    else :
        return result.append(-1)

def size():
    return result.append(len(stack))

def empty():
    if len(stack) == 0:
        return result.append(1)
    else :
        return result.append(0)

def top():
    if len(stack) != 0:
        return result.append(stack[-1])
    else :
        return result.append(-1)
    


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
    elif Input_Command[0] == "top":
        top()
    
    

for i in range(len(result)):
    print(result[i])