a, b, c = map(int, input().split())

# 물의 값 중복을 막기 위해
visited = [[0] * (b+1) for _ in range(a+1)]
# 각 물통의 초기 물의 양 (a : x, b : y, c : z)
x, y, z = 0, 0, c
# c가 가질 수 있는 물의 양
c_water = []

from collections import deque
queue = deque()

def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        queue.append((x, y))

def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        z = c - x - y
        # a 물통이 비어있는 경우 c 물통에 남아있는 양 저장
        if x == 0:
            c_water.append(z)        
             
        # x -> y
        water = min(x, b - y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c - z)
        pour(x - water, y)
        # y -> x
        water = min(y, a - x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c - z)
        pour(x, y - water)
        # z -> x
        water = min(z, a - x)
        pour(x + water, y)
        # z -> y
        water = min(z, b - y)
        pour(x, y + water)

bfs(0, 0)
c_water.sort()
for water in c_water:
    print(water, end=' ')