# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3#

# testcase1
rows, columns = 6, 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# # testcase2
# rows, columns = 3, 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# # testcase3
# rows, columns = 100, 97
# queries = [[1,1,100,97]]

def solution(rows, columns, queries):
    answer = []
    x = [i for i in range(1, columns+1)]
    board = []
    # 시작 배열 만들기
    for i in range(rows):
        b = [n + i * columns for n in x]
        board.append(b)     # 시작 배열
    for q in queries:
        x1, y1, x2, y2 = q
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        start = board[x1][y1]
        min_num = start
        for i in range(1, x2-x1+1):
            board[x1+i-1][y1] = board[x1+i][y1]
            if min_num > board[x1+i][y1]:
                min_num = board[x1+i][y1]
        for i in range(1, y2-y1+1):
            board[x2][y1+i-1] = board[x2][y1+i]
            if min_num > board[x2][y1+i]:
                min_num = board[x2][y1+i]
        for i in range(1, x2-x1+1):
            board[x2-i+1][y2] = board[x2-i][y2]
            if min_num > board[x2-i][y2]:
                min_num = board[x2-i][y2]
        for i in range(1, y2-y1):
            board[x1][y2-i+1] = board[x1][y2-i]
            if min_num > board[x1][y2-i]:
                min_num = board[x1][y2-i]
        board[x1][y1+1] = start
        answer.append(min_num)
    return answer

print(solution(rows, columns, queries))