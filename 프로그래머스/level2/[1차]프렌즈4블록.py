# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3

# # testcase1
# m, n = 4, 5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# testcase2
m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    cnt = 0
    flag = 1
    b = []
    for i in range(m):
        b.append(list(board[i]))

    while True:
        if flag == 0:
            break
        flag = 0
        # 없앨 블록 체크
        check = [[0] * n for _ in range(m)]
        # 없앨 블록 확인하고 체크박스에 저장
        for i in range(1, m):
            for j in range(1, n):
                now = b[i][j]
                if now == ' ':
                    continue
                if b[i-1][j-1] == now and b[i-1][j] == now and b[i][j-1] == now:
                    check[i-1][j-1], check[i-1][j], check[i][j-1], check[i][j] = 1, 1, 1, 1
                    flag += 1
        # 블록 없애기
        for i in range(m):
            for j in range(n):
                if check[i][j] == 1:
                    b[i][j] = ' '
                    cnt += 1

        # 블록 당겨오기
        for i in range(n):
            for j in range(m-1, 0, -1):
                if b[j][i] == ' ':
                    for k in range(j-1, -1, -1):
                        if b[k][i] != ' ':
                            b[j][i] = b[k][i]
                            b[k][i] = ' '
                            break
                    
    return cnt

print(solution(m, n, board))