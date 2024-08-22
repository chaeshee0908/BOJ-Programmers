# DFS/BFS 알고리즘
# 링크 : https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 위치 방문 표시
    visited[start] = True
    # 시작 지점의 최단 거리는 0
    distance[start] = 0
    flag = 0    # 조건에 만족하는 도시가 있는지 확인
    while queue:
        # 현재 노드 큐에서 제거
        v = queue.popleft()
        # 연결된 도시가 없을 경우
        if not graph[v]:
            continue
        # 인접 도시 찾기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                if distance[i] > distance[v] + 1:
                    distance[i] = distance[v] + 1
    # 최단 거리가 k인 도시 찾기
    for i in range(n + 1):
        if distance[i] == k:
            flag = 1
            print(i)
    if flag == 0:
        print(-1)

# 방문 확인용 1차원 리스트
visited = [False] * (n + 1)

# 최단 거리 저장 
distance = [1e9] * (n + 1)

# 시작노드 x
bfs(graph, x, visited)