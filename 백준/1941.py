import sys
from operator import itemgetter

# 회의실 배정


# 회의의 수
N = int(input())


# 회의의 내용이담길 리스트
Conf_List = []

result = 0
result_list = []
k = 0


if __name__ == "__main__":

    for i in range(N):
        start_time, end_time = map(int, sys.stdin.readline().split())
        Conf_List.append(dict(start = start_time, end = end_time))

    # Conf_List = sorted(Conf_List, key=lambda k:k['start'])
    # = sorted(Conf_List, key=itemgetter('start'))
    
    # 시작시간으로 정렬
    Conf_List.sort(key=itemgetter('start'))

    for j in range(len(Conf_List)):    
        result = 1
        k = j
        for i in range(j, len(Conf_List)):    
            if i == 0:
                continue
            elif Conf_List[i]['start'] >= Conf_List[k]['end']:
                result += 1                
                k = i
            if i == (len(Conf_List)-1):
                result_list.append(result)
                
    print(result_list)
    print(max(result_list))
    
    


    # print(Conf_List)

    