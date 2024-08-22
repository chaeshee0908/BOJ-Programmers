# 골드1 1194번
# https://www.acmicpc.net/problem/1194

import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
maze = []
door = ['A', 'B', 'C', 'D', 'E', 'F']
key = ['a', 'b', 'c', 'd', 'e', 'f']

for _ in range(N):
    maze.append(list(input()))

# 시작점 찾기
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            sx, sy = i, j

def escape_maze(sx, sy):
    q = []
    heapq.heappush(q, (0, sx, sy, ''))
    while q:
        move, x, y, now_key = heapq.heappop(q)
        # print(maze[x][y], move, now_key)
        # 도착 위치이면 반환 
        if maze[x][y] == '1':
            return move
        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 칸 내부가 아니면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽이면 패스
            if maze[nx][ny] == '#':
                # print('벽')
                continue
            # 문을 만났을 때 키가 없으면 패스
            if maze[nx][ny] in door and now_key.find(maze[nx][ny].lower()) == -1:
                # print('{}문 못열음'.format(maze[nx][ny]))
                continue
            # 문 열 경우
            # if maze[nx][ny] in door and now_key.find(maze[nx][ny].lower()) != -1:
                # print('{}문 열음'.format(maze[nx][ny]))
            # 만약 현 위치가 키이고 내가 이미 들고 있는 키가 아닐 때 
            if maze[nx][ny] in key and now_key.find(maze[nx][ny]) == -1:
                heapq.heappush(q, (move+1, nx, ny, now_key + maze[nx][ny]))
            else:
                heapq.heappush(q, (move+1, nx, ny, now_key))

    return -1

print(escape_maze(sx, sy))