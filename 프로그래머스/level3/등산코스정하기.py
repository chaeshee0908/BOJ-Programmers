# 2022 KAKAO TECH INTERNSHIP

from collections import deque

INF = int(1e9)

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    summits.sort()
    summits_set = set(summits)
    gates = set(gates)

    # 연결 내용 초기화 
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    intensity = [INF] * (n + 1)
    result = [0, INF]   # 산봉우리, 최소 intensity 
    q = deque([])
    for gate in gates:
        q.append((0, gate))
        intensity[gate] = 0

    while q:
        now_its, now = q.popleft()
        # 산봉우리 도착하거나 현재 확인하는 intensity가 찾은 최솟값보다 크면 더 이상 탐색 안함
        if now in summits_set or now_its > intensity[now]:
            continue 
        
        for next, next_its in graph[now]:
            if intensity[next] > max(now_its, next_its):
                intensity[next] = max(now_its, next_its)
                q.append((intensity[next], next))
    
    for summit in summits:
        if result[1] > intensity[summit]:
            result[1] = intensity[summit]
            result[0] = summit

    return result