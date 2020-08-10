import sys


# 로프 


# 로프 개수
N = int(input())


# 로프 리스트
rope_list = []

# 최대 중량
W_max = 0

# 중량 
W = 0

sub = 0



if __name__ == "__main__":

    for i in range(N):
        rope_list.append(int(input()))


    # 가장 무게가 가벼운 순으로 정렬
    rope_list.sort()

    for i in range(N):
        W = rope_list[i]*(N-i)
    
        if W_max < W:
            W_max = W

    print(W_max)