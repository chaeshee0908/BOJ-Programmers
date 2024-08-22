from collections import deque

# 이동 방향 : 왼, 오, 위, 아래, 왼위, 왼아래, 오위, 오아래
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    if board[x][y] == 0:
        return 0
    board[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
    return 1
                
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit(0)
    # 지도 
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    
    # 섬의 개수
    count = 0

    for i in range(h):
        for j in range(w):
            if bfs(i, j) == 1:
                count += 1
    print(count)