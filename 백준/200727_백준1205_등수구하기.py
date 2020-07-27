import sys


N, S, P = map(int, sys.stdin.readline().split())

Ranking_list = list(map(int, sys.stdin.readline().split()))

Ranking_list2 = []

Rank = 1

Ranking_list.sort(reverse=True)

# Ranking_list[0:N]

Ranking_list2.append(1)

for i in range(1, N):
    if Ranking_list[i] == Ranking_list[i-1]:
        Ranking_list2.append(Rank)
    elif Ranking_list[i] < Ranking_list[i-1]:
        Rank = i+1
        Ranking_list2.append(Rank)

#print(Ranking_list2)






Ranking_list.append(S)

Ranking_list.sort(reverse=True)


if N == 0:
    print(1)

elif Ranking_list.index(S)+1 > P:
    print(-1)
else :
    if S == Ranking_list[-1] and N==P:
        print(-1)
    else:
        print(Ranking_list.index(S)+1)











'''
for i in range(P):
    if i > (len(Ranking_list)-1):
        print(i+1)
        break
    if Ranking_list[i] > S:
        continue
    elif Ranking_list[i] == S:
        if Ranking_list[i] == Ranking_list[-1]:
            if N < P:
                print(Ranking_list2[i])
                break
            print(-1)
            break
        if i == (N-1):
            print(-1)
            break
        else :
            print(Ranking_list2[i])
            break
    elif Ranking_list[i] < S:
        print(Ranking_list2[i])
        break
'''