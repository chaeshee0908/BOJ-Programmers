# 골드 4 20056번
# https://www.acmicpc.net/problem/20056

N, M, K = map(int, input().split())
fireball = []
for _ in range(M):
    fireball.append(tuple(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def divide_fireball(board, fireball):
    new_fireball = []
    for i in range(N):
        for j in range(N):
            # 파이어볼이 같은 위치에 여러 개 일 때
            if board[i][j] > 1:
                new_m = 0
                new_s = 0
                direct = []
                for f in fireball:
                    r, c, m, s, d = f
                    if i == r and j == c:
                        new_m += m
                        new_s += s
                        direct.append(d)
                # 질량이 0이면 소멸
                if new_m//5 == 0:
                    continue
                # 방향 확인
                all_same = True
                new_d = []
                for d in direct:
                    if d % 2 == 0:
                        new_d.append(0)
                    else:
                        new_d.append(1)
                if len(set(new_d)) > 1:
                    all_same = False
                if all_same == True:
                    for a in range(4):
                        new_fireball.append((i, j, new_m//5, new_s//board[i][j], a * 2))
                else:
                    for a in range(4):
                        new_fireball.append((i, j, new_m//5, new_s//board[i][j], a * 2 + 1))
            elif board[i][j] == 1:
                for f in fireball:
                    r, c, m, s, d = f
                    if i == r and j == c:
                        new_fireball.append(f)
    return new_fireball
                        

for _ in range(K):
    # 파이어볼 이동
    next_fireball = []
    board = [[0] * N for _ in range(N)]
    while fireball:
        r, c, m, s, d = fireball.pop()
        nr = r + s * dx[d]
        nc = c + s * dy[d]
        next_fireball.append((nr, nc, m, s, d))
        board[nr][nc] += 1
    next_fireball = divide_fireball(board, next_fireball)
    fireball = next_fireball

all_m = 0
for f in fireball:
    r, c, m, s, d = f
    all_m += m

print(all_m)    
    
        
    