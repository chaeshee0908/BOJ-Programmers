# 골드3 17135
# https://www.acmicpc.net/problem/17135

from itertools import combinations
import copy

N, M, D = map(int, input().split())
main_board = []
for _ in range(N):
    main_board.append(list(map(int, input().split())))

castle = [(N, i) for i in range(M)]

# 적 성으로 한 칸 다가오기
def enemy_move():
    # 성 바로 앞 적 내려보내기
    for i in range(M):
        board[N-1][i] = 0
    # 나머지 적 내려보내기
    for i in range(N-2, -1, -1):
        for j in range(M):
            if board[i][j] == 1:
                # 적 성으로 한 칸 다가오기
                board[i][j] = 0
                board[i+1][j] = 1

# 궁수 쏠 적 찾기
def find_target(x, y):
    global D
    target = []
    for i in range(N):
        for j in range(M):
            # 궁수 공격 제한 거리안에 있는 적 발견구
            if board[i][j] == 1 and abs(x-i) + abs(y-j) <= D:
                target.append([abs(x-i) + abs(y-j), j, (i, j)])
    target.sort(key=lambda x: (x[0], x[1]))
    if not target:
        return (-1, -1)
    return target[0][2]

# 적 공격
def attack(targets, killed):
    for t in targets:
        x, y = t
        if board[x][y] == 1:
            killed += 1
            board[x][y] = 0
    return killed

# 게임 끝났는지 확인
def finish():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                return False
    return True

result = 0
for c in combinations(castle, 3):
    board = copy.deepcopy(main_board)
    killed = 0
    while not finish():
        archer_targets = []
        for x, y in c:
            if find_target(x, y) != (-1, -1):
                archer_targets.append(find_target(x, y))
        killed = attack(archer_targets, killed)
        enemy_move()
    result = max(result, killed)
        
print(result)
