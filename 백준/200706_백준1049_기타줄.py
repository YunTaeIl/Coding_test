import sys
import operator as op
from functools import reduce



# 끊어진 기타줄, M개의 브랜드
N, M = sys.stdin.readline().split()
N = int(N)
M = int(M)


# 최초 입력
A, B = sys.stdin.readline().split()
A = int(A)
B = int(B)


for i in range(int(M)-1) :
    C, D = sys.stdin.readline().split()
    C = int(C)
    D = int(D)

    if C < A :
        A = C
    if D < B :
        B = D
    

for i in range(int(N/6) + 2) :
    # 몫보다 1클때 
    if N-(i*6) < 0 :
        result4 = i*A
        break
    # 몫을 1씩 늘려가면서 값을 곱함
    result1 = i*A
    result2 = (N-(i*6))*B
    if i == 0 :
        result3 = result1 + result2

    if result3 > result1 + result2 :
        result3 = result1 + result2

    
if result4 < result3 :
    result3 = result4


print(result3)
