# https://www.acmicpc.net/problem/3184
# bfs/dfs 실버 2

import sys
input = sys.stdin.readline        
from collections import deque

r, c = map(int, input().rstrip().split())
garden = []
for _ in range(r):
    garden.append(list(input().rstrip()))

visited = [[False] * c for _ in range(r)]
# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    o, v = 0, 0
    while queue:
        x, y = queue.popleft()
        if garden[x][y] == 'o':
            o += 1
        if garden[x][y] == 'v':
            v += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and garden[nx][ny] != '#':
                queue.append((nx, ny))
                visited[nx][ny] = True
    # 양과 늑대 수 리턴
    if o <= v:
        return (0, v)
    else:
        return (o, 0)

sheep, wolf = 0, 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and garden[i][j] != '#':
            s, w = bfs(i, j)
            sheep += s
            wolf += w

print(sheep, wolf)