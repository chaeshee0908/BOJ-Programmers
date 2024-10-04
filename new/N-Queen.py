n = int(input())
count = 0
board = [[False] * n for _ in range(n)]

def pb(board, depth, now):
    print(depth, now)
    for b in board:
        print(b)
    print('-----------')

def backtracking(depth, now):
    global count
    pb(board, depth, now)
    # 세로에 queen이 있는 경우
    for i in range(depth):
        if board[i][now] == True:
            return
    # 대각선(\)에 queen이 있는 경우
    for i in range(1, min(depth, now)+1):
        if board[depth-i][now-i] == True:
            return
    # 대각선(/)에 queen이 있는 경우
    for i in range(1, min(depth, 4-now)+1):
        if depth-i < 0 or now+i >= 3:
            break
        if board[depth-i][now+i] == True:
            return

    # 전부 둔 경우
    if depth == n-1:
        count += 1
        print('합격')
        return 

    for i in range(n):
        if not board[depth][now]:
            board[depth][now] = True
            backtracking(depth+1, i)
            board[depth][now] = False

for idx in range(n):
    print(">>>>>>>>>> 현재 위치 {}에서 시작".format(idx))
    backtracking(0, idx)
print(count)