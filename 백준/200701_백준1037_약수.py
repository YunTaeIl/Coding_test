import sys
import operator as op
from functools import reduce


# N의 약수의 개수
A = sys.stdin.readline()

list1 = list(map(int, sys.stdin.readline().split()))

max_num = max(list1)
min_num = min(list1)

result2 = op.mul(max_num, min_num)

#result = reduce(op.mul, list1, 1)

print(result2)
# for _ in range(A):

    