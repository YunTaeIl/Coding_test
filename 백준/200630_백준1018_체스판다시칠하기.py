import sys
import operator as op
from functools import reduce

N, M = sys.stdin.readline().split(' ')

N = int(N) 
M = int(M)

# N이 열 M이 행
total_list = []
#cut_list1 = []
#cut_list2 = []

result = 100

# 정답 리스트
answer_list1 = [['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W']]

answer_list2 = [['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B']]


def compare(list_param):
    result1 = 0
    result2 = 0

    for i in range(8):
        for k in range(8):
            #print(cut_list2[i][k])
            #print(answer_list1[i][k])
            if(list_param[i][k] != answer_list1[i][k]):
                result1 += 1
                
    
            if(list_param[i][k] != answer_list2[i][k]):
                result2 += 1
               
            
    if result1 < result2:
        return result1
    else:
        return result2        
            



for i in range(N):
    list = sys.stdin.readline()
    total_list.append(list)

# 탐색 해야함 N이 0부터 M-8+1칸까지 M은 0부터 N-8+1칸까지
for i in range(N-8+1):
    for j in range(M-8+1):
        cut_list2 = []
        for k in range(8):
            
            cut_list1 = []
            for l in range(8):
                
                cut_list1.append(total_list[i+k][j+l])
            cut_list2.append(cut_list1)
            #print(cut_list2)
            #cut_list1.clear()
            #print(cut_list2)
        #여기에 이제 계산 
        
        temp = compare(cut_list2)
        if result > temp:
           result = temp
        #cut_list2.clear()
    

print(result)
    
        



        





