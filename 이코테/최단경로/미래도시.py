# 플로이드

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
city = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            city[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    # 서로에게 가는 시간 비용 1
    city[a][b] = 1
    city[b][a] = 1
X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            city[a][b] = min(city[a][b], city[a][k] + city[k][b])

# K나 X로 가는 경로가 없는 경우
if city[1][K] == INF or city[K][X] == INF:
    print(-1)
else:
    print(city[1][K] + city[K][X])