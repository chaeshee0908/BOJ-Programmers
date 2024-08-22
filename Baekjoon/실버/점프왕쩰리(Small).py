N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

from collections import deque

# 이동방향 : 오른쪽, 아래
dx = [0, 1]
dy = [1, 0]
visited = [[0]*N for _ in range(N)]

def bfs(board):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()

        if board[x][y] == -1:
            print('HaruHaru')
            exit(0)

        for i in range(2):
            nx = x + dx[i] * board[x][y]
            ny = y + dy[i] * board[x][y]
            if nx < N and ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
    print('Hing')

bfs(board)