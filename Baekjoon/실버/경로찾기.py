# https://www.acmicpc.net/problem/11403
# 플로이드 워셜 실버 1

import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF or graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()