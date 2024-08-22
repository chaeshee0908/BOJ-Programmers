# 프로그래머스 
# Lv3
# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
# 최단 경로 이용(힙다익스트라)

import heapq
INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))
    # 1에서의 거리
    distance = [INF] * (n+1)
    distance[0] = -1

    # 1번에서의 각각 길이 구하기
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

    # 1과 가장 먼 길이 찾기
    max_value = max(distance)
    # 1과 가장 먼 노드 개수
    cnt = distance.count(max_value)
    
    return cnt

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, edge))