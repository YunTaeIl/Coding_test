import sys
import operator as op



N = int(input())
result = 0

for i in range(1, N+1):
    if i < 100:
        result +=1
    elif i > 100:
        list_i = list(str(i))
        a = int(list_i[0])
        b = int(list_i[1])
        c = int(list_i[2])
        if c-b == b-a:
            result += 1
    
print(result)

    


