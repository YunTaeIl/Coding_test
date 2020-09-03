import sys

# 1260 DFS DFS 깊이 우선탐색, 넓이 우선탐색


# 그래프를 나타내기 위해 인접 행렬을 만들자

# N은 정점, M은 간선의 개수, V는 시작하는 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())


# 0으로 채워진 기본 행렬만듦
matrix = [[0] * (N + 1) for _ in range(N + 1)]


# 인접행렬 만들기  간선의 개수만큼 반복
for i in range(M):
    # 두 개가 연결되는건데
    link = list(map(int, sys.stdin.readline().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1



# current_node는 현재 노드의 위치 처음엔 V 시작, row는 인접행렬, foot_prints 는 결과 리스트

def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


if __name__ == "__main__":
    print(*dfs(V, matrix, []))
    print(*bfs(V))
    