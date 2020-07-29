import sys


# 입력받음
N = int(input())
N_list = list(map(int, sys.stdin.readline().split()))

# 리스트를 오름차순으로 정렬
N_list.sort()

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))


# 이분법 함수 정의
def find():
    for i in range(M):
        start = 0
        end = N
        while True :
            Mid = (start + end) // 2
            
            if M_list[i] < N_list[Mid]:
                if end == Mid:
                    print(0)
                    break
                end = Mid

            elif M_list[i] > N_list[Mid]:
                if start == Mid:
                    print(0)
                    break
                start = Mid

            elif M_list[i] == N_list[Mid]:
                print(1)
                break

    
if __name__ == "__main__":
    find()