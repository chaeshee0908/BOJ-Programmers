from collections import deque
N, K = map(int, input().split())
INF = int(1e9)

move = [-1, 1, 2]

def bfs(x):  
    q = deque([x])
    distance[x] = 0
    while q:
        x = q.popleft()
        for m in move:
            # 순간 이동
            if m == 2:
                nx = x * 2
            # 좌우 이동
            else:
                nx = x + m
            # 범위 확인 및 최단 거리 아닐 경우
            if 0 <= nx <= 100000 and distance[nx] > distance[x] + 1:
                distance[nx] = distance[x] + 1
                q.append(nx)

distance = [INF] * 100001
bfs(N)
print(distance[K])
