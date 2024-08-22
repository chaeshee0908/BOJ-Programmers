# https://www.acmicpc.net/problem/2665
# 다익스트라 골드 4

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def find_black(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '0':
            blacknum[nx][ny] += 1 

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (blacknum[x][y], x, y))
    while q:
        nowcost, now_x, now_y = heapq.heappop(q)
        if distance[now_x][now_y] < nowcost:
            continue
        for next in blacknum[now_x][now_y]:
            nextcost, next_x, next_y = next
            if nextcost == 0:
                continue
            cost = nowcost + nextcost
            if distance[next_x][next_y] > cost:
                distance[next_x][next_y] = cost
                heapq.heappush(q, (cost, next_x, next_y))
    
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
# 시작점에서부터 만나게 되는 까만 방의 최소 개수
blacknum = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        find_black(i, j)
distance = [[INF] * n for _ in range(n)]

dijkstra(0, 0)
print(distance[n-1][n-1])