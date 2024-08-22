# 골드 4 2573번
# https://www.acmicpc.net/problem/2573

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
north_pole = []
iceberg = []
for _ in range(N):
    north_pole.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if north_pole[i][j] != 0:
            iceberg.append((i, j))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    melt_ice = []
    visited[x][y] = True   
    while q:
        x, y = q.popleft()
        minus = 0   # 바다 인접 수(녹는 양)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 이동 위치가 바다이면 녹음
                if north_pole[nx][ny] == 0:
                    minus += 1
                # 이동 위치가 방문하지 않은 빙산일 때
                if visited[nx][ny] == False and north_pole[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        if minus >= 0:
            melt_ice.append((x, y, minus))
    return melt_ice 

year = -1
while True:
    count = 0
    year += 1
    visited = [[False] * M for _ in range(N)]
    melt = []
    # 1년 동안 줄을 빙산 양 체크
    for ic in iceberg:
        i, j = ic
        if visited[i][j] == False:
            melt += bfs(i, j)
            count += 1

    if count > 1:
        break
    # 빙산이 다 녹을동안 쪼개지지 않는 경우
    if count == 0:
        year = 0
        break

    next_iceberg = []
    # 빙산의 변화(녹은 빙산 반영)
    for m in melt:
        i, j, num = m
        north_pole[i][j] = max(0, north_pole[i][j] - num)
        if north_pole[i][j] > 0:
            next_iceberg.append((i, j))

    iceberg = next_iceberg

print(year)