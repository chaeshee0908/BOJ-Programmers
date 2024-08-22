# https://www.acmicpc.net/problem/11404
# 플로이드 워셜 골드 4

import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())
price = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 경우 버스 가격 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            price[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 경로의 더 작은 값으로 초기화 시켜줌
    if price[a][b] != INF:
        price[a][b] = min(price[a][b], c)
    else:
        price[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            price[a][b] = min(price[a][b], price[a][k] + price[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if price[i][j] == INF:
            print(0, end=' ')
        else:
            print(price[i][j], end=' ')
    print()