import sys

# 2606 바이러스 DFS BFS 깊이 우선탐색, 넓이 우선탐색


# N은 컴퓨터의 수 
N = int(input())

# 컴퓨터의 쌍의 수
M = int(input())

# 컴퓨터 번호 쌍 list
V = []
for i in range(M):
    V.append(list(map(int, sys.stdin.readline().split())))


# 인접행렬을 만들기 위해 0으로 채워진 행렬을 만듦 인덱스를 위해 컴퓨터수 + 1만큼의 행렬을 만들어야함
matrix = [[0]*(N+1) for _ in range(N+1)]

# 인접행렬 만들기
for i in range(M):
    matrix[V[i][0]][V[i][1]] = 1
    matrix[V[i][1]][V[i][0]] = 1
    


# 결국 DFS든 BFS든을 통해 찾아야함
def BFS():
    # 1은 시작하는 번호
    queue = [1]
    result = [1]
    while queue:
        # 제일 처음에 있는거 빼고 현재 노드에 저장
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] == 1 and search_node not in result:
                result += [search_node]
                queue += [search_node]
    return result

    



# N, M, V = map(int, sys.stdin.readline().split())

if __name__ == "__main__":
    #print(V)
    #print(matrix)
    print(len(BFS())-1)

