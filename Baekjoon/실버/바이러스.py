# 2606번 (실버3)
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 연결 쌍의 수
c = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(c):
    i, j = map(int, input().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt

print(bfs(graph, 1, visited))