import sys


M = int(input())
N = int(input())


result_list = []
result = 0
result_add = 0


# 소수야?
def Disinction(num):

    
    if num == 2:
        result_list.append(num)
        return
    

    for i in range(2, num):
        if (num % i) == 0 :
            break
        elif i == num-1 :
            result_list.append(num)
    
        

if __name__ == "__main__":
    for i in range(M, N+1):
        Disinction(i)

    if len(result_list) == 0:
        result = -1
    else:
        for i in range(len(result_list)):
            result_add += result_list[i]
        print(result_add)
        result = result_list[0]
    
    #print(result_list)
    print(result)