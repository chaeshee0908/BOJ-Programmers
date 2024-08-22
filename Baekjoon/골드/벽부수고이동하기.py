# 2206번 (골드4)
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
goal = graph[n-1][m-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = 0    # 벽을 한 번만 부실 수 있도록

def bfs(x, y):
    global flag
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if graph[nx][ny] == 1:
                if flag == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                    flag = 1
                else:
                    continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    if graph[n - 1][m - 1] == goal:
        return -1
    else:
        return graph[n - 1][m - 1]


print(bfs(0,0))
