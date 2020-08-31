import sys
import operator as op


# 10866 덱


# 입력받는 명령 수 
N = int(input())

# 결과 값 리스트
result = []

# 데크 리스트
Deque = []



def push_front(X):
    Deque.insert(0, X)

def push_back(X):
    Deque.append(X)

def pop_front():
    if len(Deque) == 0:
        result.append(-1)
    else:
        result.append(Deque.pop(0))
    

def pop_back():
    if len(Deque) == 0:
        result.append(-1)
    else:
        result.append(Deque.pop())

def size():
    result.append(len(Deque))

def empty():
    if len(Deque) == 0:
        result.append(1)
    else:
        result.append(0)
    

def front():
    if len(Deque) == 0:
        result.append(-1)
    else:
        result.append(Deque[0])

def back():
    if len(Deque) == 0:
        result.append(-1)
    else:
        result.append(Deque[-1])
    


if __name__ == "__main__":
    
    for i in range(N):
        Input_Command = list(sys.stdin.readline().split())
    
        if len(Input_Command) == 2:
            Input_X = int(Input_Command[1])
            if Input_Command[0] == "push_back":
                push_back(Input_X)
            else :
                push_front(Input_X)
        elif Input_Command[0] == "pop_front":
            pop_front()
        elif Input_Command[0] == "pop_back":
            pop_back()
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
    