# https://www.acmicpc.net/problem/2617
# 플로이드 워셜 골드 5

# 크거나 작은 구슬의 개수가 N/2보다 크다면 중간값이 될 수 없다
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy][light] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

cnt = 0

for i in range(1, N + 1):
    left = 0
    right = 0
    for j in range(1, N + 1):
        # 무겁다고 표시된 경우
        if graph[i][j] == 1:
            right += 1
        # 가볍다고 표시된 경우
        elif graph[j][i] == 1:
            left += 1
    # 가볍거나 무거운 개수가 중간값보다 많으면 중간값이 될 수 없는 경우
    if right > N//2 or left > N//2:
        cnt += 1

print(cnt)