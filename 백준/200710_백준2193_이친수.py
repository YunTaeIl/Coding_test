# 자리수
N = int(input())

b = [1, 1]
result = 0

if N == 1:
    result = 1
elif N == 2:
    result = 1
elif N >= 3:
    for i in range(2,N):
        b.append(b[-1] + b[-2])
    result = b[-1]


print(result)
