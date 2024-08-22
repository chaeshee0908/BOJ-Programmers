# 골드3 17779
# https://www.acmicpc.net/problem/17779

N = int(input())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))
INF = int(1e9)

from itertools import product
from collections import deque

numbers = [i for i in range(N+1)]
result = INF
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_boundary(x, y, d1, d2):
    boundary1 = [(x + i, y - i) for i in range(d1+1)]
    boundary2 = [(x + i, y + i) for i in range(d2+1)]
    boundary3 = [(x + d1 + i, y - d1 + i) for i in range(d2+1)]
    boundary4 = [(x + d2 + i, y + d2 - i) for i in range(d1+1)]
    all_boundary = list(set(boundary1 + boundary2 + boundary3 + boundary4))
    for boundary in all_boundary:
        r, c = boundary
        area_info[r][c] = 5
    
    return all_boundary

def check_area5(boundary):
    boundary_dict = {}
    for b in boundary:
        x, y = b
        if x in boundary_dict:
            boundary_dict[x].append(y)
        else:
            boundary_dict[x] = [y]
    
    # 경계선 안을 5로 채우기
    for k in boundary_dict.keys():
        if len(boundary_dict[k]) == 1:
            continue
        start, end = min(boundary_dict[k]), max(boundary_dict[k])
        for i in range(start + 1, end):
            area_info[k][i] = 5

def check_other_area(sx, sy, ex, ey, area_num):
    q = deque([])
    # 4일때만 끝지점에서 탐색
    if area_num == 4:
        q.append((ex, ey))
        area_info[ex][ey] = area_num
    else:
        q.append((sx, sy))
        area_info[sx][sy] = area_num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if sx <= nx <= ex and sy <= ny <= ey and area_info[nx][ny] == 0:
                area_info[nx][ny] = area_num
                q.append((nx, ny))

def check_area_people():
    for i in range(N):
        for j in range(N):
            area_people[area_info[i][j]-1] += city[i][j]

for p in product(numbers, repeat=4):
    x, y, d1, d2 = p
    # 기준점이 재현시 밖이거나 이동 거리가 0일 때 
    if x == N or y == N or d1 == 0 or d2 == 0:
        continue
    # 경계 중 한 값이라도 재현시 밖일 때
    if x + d1 >= N or y - d1 < 0 or x + d2 >= N or y + d2 >= N or x + d2 + d1 >= N or y + d2 - d1 < 0 or y + d2 - d1 >= N:
        continue
    area_info = [[0] * N for _ in range(N)]
    area_people = [0] * 5
    boundary = check_boundary(x, y, d1, d2)
    check_area5(boundary)   # 5구역 체크
    check_other_area(0, 0, x + d1 - 1, y, 1)       # 1구역 체크
    check_other_area(0, y + 1, x + d2, N-1, 2)      # 2구역 체크
    check_other_area(x + d1, 0, N-1, y - d1 + d2 - 1, 3)   # 3구역 체크
    check_other_area(x + d2 + 1, y - d1 + d2, N-1, N-1, 4) # 4구역 체크
    check_area_people() # 구역별 사람수 확인
    area_people.sort()
    diff = area_people[4] - area_people[0]  # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이
    result = min(result, diff)

print(result)