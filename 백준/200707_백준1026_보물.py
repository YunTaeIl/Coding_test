import sys
import operator as op
from itertools import product
from itertools import permutations

# 배열의 크기
N = int(input())


# 배열을 입력받음
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 정렬
A.sort(reverse=True)


# 정답 
result3 = 10000

result2 = 0


for i in range(N):
    result = A[i]*min(B)
    B.remove(min(B))
    result2 += result


print(result2)

