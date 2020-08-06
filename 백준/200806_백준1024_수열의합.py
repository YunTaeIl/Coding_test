import sys

# 수열의 합



# N과 L입력받기
N, L = map(int, sys.stdin.readline().split())

result_list = []

if __name__ == "__main__":

    
    for i in range(L, 101):
        
        x = int((2*N - (i*i - i))/(2*i))
        result_list = list(range(x, x+i))
        if sum(result_list) == N:
            result_list = list(range(x, x+i))
            break
       

    
    if not result_list or result_list[0]<0 or sum(result_list) != N:
        print(-1)
    else:
        for i in range(len(result_list)):
            if i == (len(result_list)-1) :
                print(result_list[i])
            else : 
                print(result_list[i], end=' ')
