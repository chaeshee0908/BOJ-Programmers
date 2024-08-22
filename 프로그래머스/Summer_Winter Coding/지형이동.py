#Lv4
# 격자 입력받기
N, height = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

import heapq

# 위치 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(land, height):
    # 최소 비용
    cost = 0
    # 가로, 세로 길이
    n = len(land)
    # 방문 확인
    visited = [[False] * n for _ in range(n)]
    heap = [[0, 0, 0]]

    while heap:
        v, x, y = heapq.heappop(heap)
        if visited[x][y] == True:
            continue
        print('------------------------------')
        print('v:',v)
        for a in visited:
            print(a)
        print('------------------------------')
        visited[x][y] = True
        cost += v
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 사다리 없이 이동 가능
                if abs(land[x][y] - land[nx][ny]) <= height:
                    heapq.heappush(heap, [0, nx, ny])
                # 사다리가 필요한 경우 (가장 최소 비용 찾아줌)
                else:
                    if abs(land[x][y] - land[nx][ny]) > height:
                        heapq.heappush(heap, [abs(land[x][y] - land[nx][ny]), nx, ny])
    return cost


print(solution(land, height))