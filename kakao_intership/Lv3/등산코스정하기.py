import heapq
INF = int(1e9)

def dijkstra(n, start, graph, gates, summits):
    intensity = [INF] * (n+1)
    # 산봉우리를 한 번만 거치는지 확인하기 위한 리스트
    flag = [0] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    intensity[start] = 0
    while q:
        its, now = heapq.heappop(q)
        # 해당 산봉우리를 이미 거친 경우
        if flag[now] == 1:
            continue
        # 이미 방문한 적 있는 노드일 경우
        if intensity[now] < its:
            continue
        for node, dist in graph[now]:
            # 게이트일 경우
            if node in gates:
                continue
            # intensity는 가장 오래 걸리는 거리
            cost = max(dist, its)
            # 그 중 가장 짧은 것 찾기
            if intensity[node] > cost:
                intensity[node] = cost
                heapq.heappush(q, (cost, node))
                if node in summits:
                    flag[node] = 1
    s_intensity = []
    for i in range(1, n+1):
        if i in summits:
            heapq.heappush(s_intensity, (intensity[i], i))
    return heapq.heappop(s_intensity)
            


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    # 모든 경로 정보 초기화
    for p in paths:
        n1, n2, cost = p
        graph[n1].append((n2, cost))
        graph[n2].append((n1, cost))
    min_intensity = INF
    summits.sort()
    summits_set = set(summits)
    summit = 0
    # 출입구 별로 진행
    for g in gates:
        result = dijkstra(n, g, graph, gates, summits_set)
        value, node_num = result
        if value < min_intensity:
            summit = node_num
            min_intensity = value
    return [summit, min_intensity]

n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]
print(solution(n, paths, gates, summits))
