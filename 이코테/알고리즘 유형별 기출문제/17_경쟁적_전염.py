# DFS/BFS 알고리즘
# 링크 : https://www.acmicpc.net/problem/18405

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().rstrip().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().rstrip().split())))
s, x, y = map(int, input().rstrip().split())
virus = [[] for _ in range(k + 1)]      # 바이러스 위치정보
for i in range(n):
    for j in range(n):
        v = array[i][j]
        if v != 0:
            virus[v].append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, v_num):
    new_virus = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 바이러스가 없는 곳이면
            if array[nx][ny] == 0:
                array[nx][ny] = v_num   # 해당 바이러스 넘버 넣어줌
                new_virus.append((nx, ny))
    virus[v_num] = new_virus
            
# s초 동안
for _ in range(s):
    for i in range(1, k+1):
        for v in virus[i]:
            a, b = v
            bfs(a, b, i)
    
for i in range(n):
    print(array[i])
print(array[x-1][y-1])
