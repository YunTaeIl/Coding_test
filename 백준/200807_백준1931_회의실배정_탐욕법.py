import sys
from operator import itemgetter

# 회의실 배정


# 회의의 수
N = int(input())


# 회의의 내용이담길 리스트
Conf_List = []

temp = 0
result = 0

if __name__ == "__main__":

    for i in range(N):
        start_time, end_time = map(int, sys.stdin.readline().split())
        Conf_List.append(dict(start = start_time, end = end_time))
   
    # 끝나는시간으로 정렬
    Conf_List.sort(key=itemgetter('start'))
    Conf_List.sort(key=itemgetter('end'))
    
    #print(Conf_List)

    j = 0
    i = 1 
    while i < len(Conf_List) :    
        if Conf_List[i]['start'] < Conf_List[j]['end']:
            del Conf_List[i]
        else :
            j = i
            i += 1

    print(len(Conf_List))