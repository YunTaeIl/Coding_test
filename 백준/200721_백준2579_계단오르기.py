import sys
import operator as op

# 계단의 수
Stairs_Num = int(input())
Stairs_Score = []
DP_Score = []

# 계단 각각의 점수
for i in range(Stairs_Num):
    Stairs_Score.append(int(input()))

def dp(): 
    if Stairs_Num == 1:
        DP_Score.append(Stairs_Score[0])
        return
    if Stairs_Num == 2:
        DP_Score.append(Stairs_Score[0])
        DP_Score.append(max(Stairs_Score[0] + Stairs_Score[1], Stairs_Score[1]))
        return
    DP_Score.append(Stairs_Score[0])
    DP_Score.append(max(Stairs_Score[0] + Stairs_Score[1], Stairs_Score[1]))
    DP_Score.append(max(Stairs_Score[1] + Stairs_Score[2], Stairs_Score[0] + Stairs_Score[2]))
    for i in range(3, Stairs_Num):
        DP_Score.append(max(DP_Score[i-3]+Stairs_Score[i-1]+Stairs_Score[i], DP_Score[i-2] + Stairs_Score[i]))
    

dp()

print(DP_Score[-1])