# 골드5 14503번
# https://www.acmicpc.net/problem/14503

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
place = []
for _ in range(N):
    place.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, d):
    q = deque([])
    q.append((x, y, d))
    place[x][y] = 2
    cnt = 1 # 청소한 칸의 개수
    while q:
        x, y, d = q.popleft()
        # 현재 위치한 칸이 청소가 안 되어 있는 경우
        if place[x][y] == 0:
            place[x][y] = 2 # 청소하면 2
            cnt += 1
        # 현재 위치한 칸이 청소가 되어 있는 경우
        if place[x][y] == 2:
            clean = True
            for i in range(1, 5):
                now_d = ((d - i) + 4) % 4   # 반시계 방향으로 90도 회전
                nx = x + dx[now_d]
                ny = y + dy[now_d]
                # 현재 칸의 주변 4칸 중 청소되지 않은 칸이 있는 경우
                if 0 <= nx < N and 0 <= ny < M and place[nx][ny] == 0:
                    clean = False
                    place[nx][ny] = 2
                    cnt += 1
                    q.append((nx, ny, now_d))
                    break
            # 현재 칸의 주변 4칸 중 청소되지 않은 칸이 없는 경우
            if clean == True:
                back = (d + 2) % 4  # 후진 방향
                nx = x + dx[back]
                ny = y + dy[back]
                # 후진하면 벽에 부딪히는 경우
                if 0 <= nx < N and 0 <= ny < M and place[nx][ny] == 1:
                    return cnt  # 작동을 멈춘다
                else:
                    q.append((nx, ny, d))   # 방향은 같음
    return cnt

print(bfs(r, c, d))