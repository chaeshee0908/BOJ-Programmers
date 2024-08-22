# https://www.acmicpc.net/problem/2458
# 플로이드 워셜 골드 4

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
heights = [[INF] * (N + 1) for _ in range(N + 1)] 

for _ in range(M):
    a, b = map(int, input().split())
    # a가 b보다 더 키가 작다
    heights[a][b] = 1 

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if heights[i][k] + heights[k][j] == 2:
                heights[i][j] = 1

cnt = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if heights[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1

print(cnt.count(N - 1))