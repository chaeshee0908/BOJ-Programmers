from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
virus = []
d = [[] for _ in range(k + 1)]
cnt = 0

for i in range(n):  # 지도 입력 받음
    input = list(map(int, stdin.readline().split()))
    virus.append(input)
    for j in range(n):
        if input[j]:
            d[input[j]].append((i, j))

s, x, y = map(int, stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(k, tuple):
    queue = deque()
    while tuple:
        queue.append(tuple.pop())
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 범위 넘는 경우 패스
                continue
            if virus[nx][ny] == 0:
                virus[nx][ny] = k
                tuple.append((nx, ny))

for _ in range(s):
    for i in range(1, k + 1):
        bfs(i, d[i])

for i in range(n):
    print(virus[i])
print(virus[x-1][y-1])