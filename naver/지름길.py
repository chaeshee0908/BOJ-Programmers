import heapq
INF = int(1e9)

N, D = map(int, input().split())
# 경로 설정
graph = [[] for _ in range(D+1)]
for i in range(1, D+1):
    # 목적지, 경로길이 
    graph[i].append((i+1, 1))

# 지름길 경로 설정
for _ in range(N):
    start, end, length = map(int, input().split())
    # 역주행 불가
    if end > D:
        continue
    graph[start].append((end, length))

distance = [INF] * 10001
def dijkstra():
    distance[0] = 0
    q = []
    heapq.heappush(q, (distance[0], 0))
    while q:
        now_dist, now = heapq.heappop(q)
        # 이미 최단거리이면 패스
        if distance[now] < now_dist:
            continue
        for next, next_dist in graph[now]:
            cost = now_dist + next_dist
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra()
print(distance[D])