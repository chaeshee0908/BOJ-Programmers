# 골드 4 9207번
# https://www.acmicpc.net/problem/9207

def play_game():
    

N = int(input())

for _ in range(N):
    board = []
    while True:
        line = list(input())
        if not line:
            break
        board.append(line)
    n, m = len(board), len(board[0])
    

    
