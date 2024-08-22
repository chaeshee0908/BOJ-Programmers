# 1260번 (실버2)
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque
from sys import stdin

input = stdin.readline

def bfs(graph, start, visited):
    global b_ans
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        b_ans.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    global d_ans
    visited[v] = True
    d_ans.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, v = map(int, input().rstrip().split())
graph = [[9999]*(n+1) for _ in range(n+1)]
b_visited = [False] * (n+1)
d_visited = [False] * (n+1)

for i in range(n+1):
    graph[i][i] = 0
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    graph[i][j], graph[j][i] = 1, 1
f_graph = [[]]

for i in range(1,n+1):
    f_graph.append([j for j in range(1, n+1) if graph[i][j] == 1])

b_ans = []
d_ans = []

dfs(f_graph, v, d_visited)
bfs(f_graph, v, b_visited)

for i in d_ans:
    print(i, end=' ')
print()
for i in b_ans:
    print(i, end=' ')