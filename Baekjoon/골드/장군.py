# 골드5 16509번
# https://www.acmicpc.net/problem/16509

# 상 위치
sx, sy = map(int, input().split())
# 왕 위치
kx, ky = list(map(int, input().split()))

# 상좌, 상우, 하좌, 하우, 좌상, 좌하, 우상, 우하
dx = [[-1, -1, -1], [-1, -1, -1], [1, 1, 1], [1, 1, 1], [0, -1, -1], [0, 1, 1], [0, -1, -1], [0, 1, 1]]
dy = [[0, -1, -1], [0, 1, 1], [0, -1, -1], [0, 1, 1], [-1, -1, -1], [-1, -1, -1], [1, 1, 1], [1, 1, 1]]

dist = [[0] * 9 for _ in range(10)]

from collections import deque

def bfs():
    q = deque([])
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        # 왕에 도달
        if x == kx and y == ky:
            return dist[x][y]
        for i in range(8):
            flag = True
            nx, ny = x, y
            for j in range(3):
                nx += dx[i][j]
                ny += dy[i][j]
                # 장기판 밖으로 이동할 때
                if nx < 0 or nx >= 10 or ny < 0 or ny >= 9:
                    flag = False
                    break
                # 이동 경로에 다른 기물(왕)이 있을 시
                if j != 2 and nx == kx and ny == ky:
                    flag = False
                    break
            # 이동 가능한 칸이고 아직 방문하지 않았다면
            if flag == True and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1   # 최단 거리 표시 
                q.append((nx, ny))
        
    # 왕에게 도달 불가 시
    return -1

print(bfs())