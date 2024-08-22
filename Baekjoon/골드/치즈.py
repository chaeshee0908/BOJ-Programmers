# https://www.acmicpc.net/problem/2636
# bfs/dfs 골드 5

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

visited = [[False] * m for _ in range(n)]
# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_all():
    for i in range(n):
        if False in visited[i]:
            return True
    return False

def bfs():
    global flag
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    cheeze = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                # 치즈 녹이기
                if board[nx][ny] == 2:
                    board[nx][ny] = 0
                    queue.append((nx, ny))
                elif board[nx][ny] == 0:
                    queue.append((nx, ny))
                if board[nx][ny] == 1:
                    flag = 1
                    board[nx][ny] = 2   # 녹을 치즈
                    cheeze += 1
    return cheeze

hour = 0
cheeze_num = 0

while check_all():
    visited = [[False] * m for _ in range(n)]
    flag = 0       # 남은 치즈가 있는지 확인
    cheeze = bfs()
    # 다 녹기전 마지막 치즈 개수
    if cheeze != 0:
        cheeze_num = cheeze
    # 남은 치즈가 있었다면 시간 추가
    if flag == 1:
        hour += 1

print(hour)
print(cheeze_num)