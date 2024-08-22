# https://www.acmicpc.net/problem/1446
# 다익스트라 실버 1

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 지름길의 개수 N, 고속도로의 길이 D
N, D = map(int, input().split())
# 고속도로와 지름길의 정보
graph = [[] for _ in range(D + 1)]
# 모든 지름길 정보 입력
for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, length))
distance = [INF] * (D + 1)

# 모든 길 연결
for i in range(D):
    graph[i].append((i + 1, 1))

dijkstra(0)
print(distance[-1])