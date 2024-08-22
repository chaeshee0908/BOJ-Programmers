# 골드1 18809번
# https://www.acmicpc.net/problem/18809

from itertools import combinations
import copy

N, M, G, R = map(int, input().split())
garden = []
result = 0  # 꽃의 최대 개수
for _ in range(N):
    garden.append(list(input().split()))

plant_position = [] # 배양액 뿌릴 수 있는 땅 위치

for i in range(N):
    for j in range(M):
        # 배양액 뿌릴 수 있는 곳 찾기 
        if garden[i][j] == '2':
            plant_position.append((i, j))

# 배양액 뿌리기
def sprinkle(green, red):
    new_garden = copy.deepcopy(garden)
    for g in green:
        x, y = g
        new_garden[x][y] = 'g'    # 초록배양액 뿌린 곳 g
    
    for r in red:
        x, y = r    
        new_garden[x][y] = 'r'  # 빨강배양액 뿌린 곳 r
    
    return new_garden

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배양액 퍼지기
def spread(x, y, new_garden, next_position):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and (new_garden[nx][ny] == '1' or new_garden[nx][ny] == '2'):
            next_position.append((nx, ny))
    
    return next_position

# 꽃 피는지 확인
def flowering(green, red):
    flower_position = []
    for g in green:
        if g in red:
            flower_position.append(g)
    return flower_position

# garden 출력
def pp(new_garden):
    print('----------------------------')
    for i in range(N):
        for j in range(M):
            print(new_garden[i][j], end=' ')
        print()

for green_position in combinations(plant_position, G):
    remain_position = tuple(set(plant_position) - set(green_position))
    for red_position in combinations(remain_position, R):
        new_garden = sprinkle(green_position, red_position)
        print(green_position, red_position)
        f_num = 0
        while True:
            now_green = []  
            now_red = []
            next_green = []
            next_red = []
            # 정원에 현재 포함된 배양액 위치 확인 
            for i in range(N):
                for j in range(M):
                    if new_garden[i][j] == 'g':
                        now_green.append((i, j))
                    elif new_garden[i][j] == 'r':
                        now_red.append((i, j))
            # 배양액 퍼지기
            for ng in now_green:
                x, y = ng
                next_green = spread(x, y, new_garden, next_green)
            for nr in now_red:
                x, y = nr
                next_red = spread(x, y, new_garden, next_red)
            # 더 이상 배양액이 퍼질 수 없으면 종료
            if not next_green and not next_red:
                break
            # 꽃 핀 위치 확인
            flower_position = flowering(next_green, next_red)
            for f in flower_position:
                x, y = f
                new_garden[x][y] = 'f'
                f_num += 1
            # 배양액 위치 표시하기
            for neg in next_green:
                x, y = neg
                if new_garden[x][y] != 'f': # 꽃 피는 위치가 아니면
                    new_garden[x][y] = 'g'
            for ner in next_red:
                x, y = ner
                if new_garden[x][y] != 'f': # 꽃 피는 위치가 아니면
                    new_garden[x][y] = 'r'
        result = max(result, f_num)
        print(f_num)
        print('------------------')
print(result)