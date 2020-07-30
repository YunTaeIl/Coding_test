import sys
from itertools import product
from itertools import permutations

# 사람의 수
N = int(input())

# 모든 사람이 인출시 걸리는시간
result = 0

# 모든 사람의 경우의 수
per_ATM = []

# 최솟값을 찾기위한 result 리스트
result_min = []

def calcu(ATM):
    # 각 사람이 인출시 걸리는 시간
    P = []
    P.append(ATM[0])
    result = P[0]
    for i in range(1, N):
        P.append(ATM[i] + P[i-1])
        result += P[i]
    result_min.append(result)


if __name__ == "__main__":

    ATM_list = list(map(int, sys.stdin.readline().split()))
    
    ATM_list.sort()
    calcu(ATM_list)
    print(result_min[0])


    '''
    per_ATM = list(permutations(ATM_list, N))
    for x in per_ATM:
        calcu(x)
    print(min(result_min))
    '''
    #calcu()
    #print(ATM_list)
    #print(P)
