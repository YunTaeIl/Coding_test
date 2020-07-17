import sys
import math


# X는 게임횟수 Y는 이긴횟수 
X, Y = sys.stdin.readline().split()
X = int(X)
Y = int(Y)
#Z = math.trunc((Y/X)*100)
Z = math.trunc((100*Y/X))
W = 1000000000
# W = 추가 게임수

#포인트 확률이 바뀔수 없는 경우는 99퍼센트이상일때
def search():
    start = 0
    end = W
    while start <= end :
        mid = (start + end) // 2
        
        if math.trunc(((Y+mid)/(X+mid))*100) > Z :
            end = mid - 1
        else :
            start = mid + 1
    print(end + 1)


if Z >= 99:
    print(-1)
else:
    search()


