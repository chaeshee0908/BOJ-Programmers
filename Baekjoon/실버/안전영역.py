# https://www.acmicpc.net/problem/2468
# bfs/dfs 실버1

import sys
sys.setrecursionlimit(100000)

n = int(input())
area = []
max_num, min_num = 0, 100
for _ in range(n):
    a = list(map(int, input().split()))
    area.append(a)
    if max_num < max(a):
        max_num = max(a)
    if min_num > min(a):
        min_num = min(a)

def dfs(x, y, h):
    # 주어진 범위를 넘어갈 경우 즉시 종료
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    # 아직 방문하지 않았다면 / 잠기지 않는다면 
    if not visited[x][y] and area[x][y] > h:
        visited[x][y] = True
        dfs(x - 1, y, h)
        dfs(x + 1, y, h)
        dfs(x, y - 1, h)
        dfs(x, y + 1, h)
        return True 
    return False       

# 안전한 영역의 최대 개수 
max_area = 0

for h in range(min_num - 1, max_num + 1):
    num = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, h) == True:
                num += 1
    if max_area < num:
        max_area = num

print(max_area)
        
                