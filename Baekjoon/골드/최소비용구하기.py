# https://www.acmicpc.net/problem/1916
# 다익스트라 골드 5

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    bus_cost[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if bus_cost[now] < cost:
            continue
        for nextNum, nextCost in graph[now]:
            c = cost + nextCost
            if bus_cost[nextNum] > c:
                bus_cost[nextNum] = c
                heapq.heappush(q, (c, nextNum))

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # a 도시에서 출발하여 b 도시로 갈 때 드는 버스 비용
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
start, finish = map(int, input().split())
bus_cost = [INF] * (N + 1)
dijkstra(start)
print(bus_cost[finish])