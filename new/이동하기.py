import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*M for _ in range(N)]
maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))

dp[0][0] = maze[0][0]

for i in range(N):
    for j in range(M):
        if i >= 1 and j >= 1:
            dp[i][j] = maze[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        elif i >= 1:
            dp[i][j] = maze[i][j] + dp[i-1][j]
        elif j >= 1:
            dp[i][j] = maze[i][j] + dp[i][j-1]

print(dp[N-1][M-1])