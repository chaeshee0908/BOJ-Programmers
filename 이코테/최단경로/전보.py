# 다익스트라

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        nowdist, nowcity = heapq.heappop(q)
        if distance[nowcity] < nowdist:
            continue
        for next in city[nowcity]:
            nextcity, nextdist = next
            cost = nowdist + nextdist
            if distance[nextcity] > cost:
                distance[nextcity] = cost
                heapq.heappush(q, (cost, nextcity))


# 도시의 개수 N, 통로의 개수 M
N, M, C = map(int, input().split())
city = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    city[x].append((y, z))
distance = [INF] * (N + 1)

# 메세지를 받는 도시의 개수
cnt = 0
# 총 걸리는 시간
time = 0
dijkstra(C)
for i in range(1, N + 1):
    if distance[i] != INF and distance[i] != 0:
        cnt += 1
        time = max(time, distance[i])
print(cnt, time)
        