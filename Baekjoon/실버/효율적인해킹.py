# https://www.acmicpc.net/problem/1325
# bfs/dfs 실버1

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
from collections import deque

# 컴퓨터 개수, 신뢰 관계 수
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt

count = []

for i in range(1, n+1):
    count.append(bfs(i))

c_num = max(count)

for i, num in enumerate(count):    
    if num == c_num:
        print(i + 1, end=' ')