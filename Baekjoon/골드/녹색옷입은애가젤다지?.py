# https://www.acmicpc.net/problem/4485
# 다익스트라 골드 4

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(x, y):
    q = []
    # 검정 루피 값, x, y 값
    heapq.heappush(q, (cave[x][y], 0, 0))
    blackRupee[x][y] = cave[x][y]
    while q:
        now_cost, now_x, now_y = heapq.heappop(q)
        if now_x == N - 1 and now_y == N - 1:
            print('Problem {}: {}'.format(count, now_cost))
            break
        if blackRupee[now_x][now_y] < now_cost:
            continue
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            # 위치가 동굴 내부를 이탈하지 않을 시
            if 0 <= next_x < N and 0 <= next_y < N:
                next_cost = now_cost + cave[next_x][next_y]
                # 다음 위치까지의 검정루피를 더 작은 값으로 변경
                if next_cost < blackRupee[next_x][next_y]:
                    blackRupee[next_x][next_y] = next_cost
                    heapq.heappush(q, (next_cost, next_x, next_y))

count = 0

while True:
    N = int(input())
    if N == 0:
        break
    count += 1
    cave = []
    for _ in range(N):
        cave.append(list(map(int, input().split())))
    blackRupee = [[INF] * (N + 1) for _ in range(N + 1)]
    dijkstra(0, 0)