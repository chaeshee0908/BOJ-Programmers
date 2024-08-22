# 골드5 15686번
# https://www.acmicpc.net/problem/15686

N, M = map(int, input().split())
city = []
chicken = []
home = []
for i in range(N):
    city.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            home.append((i, j))

from itertools import combinations

def chicken_distance(c):
    total_distance = 0
    for h in home:
        hx, hy = h
        min_d = 2 * N
        for t in c:
            cx, cy = t
            d = abs(cx - hx) + abs(cy - hy)
            min_d = min(min_d, d)
        total_distance += min_d
    return total_distance

result = int(1e9)
for c in combinations(chicken, M):
    distance = chicken_distance(c)
    result = min(result, distance)

print(result)