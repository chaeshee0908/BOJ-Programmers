import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def bfs():
    q = deque()
    q.append((0, 0))
    result = int(1e9)
    visited = [False] * N
    visited[0] = True
    while q:
        x, cnt = q.popleft()
        if x == N-1:
            result = min(result, cnt)
        for i in range(1, board[x]+1):
            nx = x + i
            if 0 <= nx < N and not visited[nx]:
                q.append((nx, cnt + 1))
                visited[nx] = True
    return result

N = int(input())
board = list(map(int, input().split()))
result = bfs()
if result == INF:
    print(-1)
else:
    print(result)