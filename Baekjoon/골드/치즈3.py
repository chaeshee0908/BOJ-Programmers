# 골드3 2638번
# https://www.acmicpc.net/problem/2638

from collections import deque

N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 치즈 내부 공간: 0, 치즈 외부 공간: 2, 치즈: 1
def outside():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    if paper[0][0] == 0:
        paper[0][0] = 2
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and paper[nx][ny] != 1:
                visited[nx][ny] = True
                paper[nx][ny] = 2
                q.append((nx, ny))

# 외부와 2면이상 맞닿은 치즈 녹이기
def melt(x, y):
    out = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and paper[nx][ny] == 2:
            out += 1
    # 외부와 2면 이상 접촉 -> 녹음
    if out >= 2:
        paper[x][y] = -1

result = 0
finish = False
while not finish:
    finish = True
    visited = [[False] * M for _ in range(N)]
    outside()
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:
                finish = False
                melt(i, j)
    if finish == False:
        result += 1
            
print(result)