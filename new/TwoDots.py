import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    if x < 0 or x >= N or y < 0 or y >= M or board[x][y] != board[sx][sy]:
        return False
    # 사이클 가능
    if x == sx and y == sy and cnt >= 4:
        return True
    if visited[x][y] == True:
        return False
    if visited[x][y] == False:
        visited[x][y] = True
        if dfs(x-1, y, cnt+1) or dfs(x, y-1, cnt+1) or dfs(x+1, y, cnt+1) or dfs(x, y+1, cnt+1):
            return True
    return False 
    

result = False
for i in range(N):
    for j in range(M):
        now_color = board[i][j]
        # 사이클이 생기는 최소한의 조건(현재 위치 오른쪽과 아래에 같은 색 점이 있어야함)
        if not(j+1 < M and i+1 < N and board[i][j+1] == now_color and board[i+1][j] == now_color):
            continue
        visited = [[False]*M for _ in range(N)]
        sx, sy = i, j
        if dfs(i, j, 1):
            result = True
            break
    if result:
        break

print("Yes" if result else "No")