# 프로그래머스
# Lv2
# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

def solution(maps):
    # 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 세로, 가로 길이
    n, m = len(maps), len(maps[0])

    # 최단 거리 구하기(dfs)
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 위치가 지도 안에 없으면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동할 위치가 벽이면 무시
            if maps[nx][ny] == 0:
                continue
            # 아직 방문하지 않은 곳이라면 최단 거리 등록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    print(maps)
    # 상대 진영에 도달할 수 있으면 최단 거리 반환
    if maps[n-1][m-1] != 1:
        return maps[n-1][m-1]
    # 상대 진영에 도달할 수 없으면 -1 반환
    else:
        return -1     


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
print(solution(maps))
    