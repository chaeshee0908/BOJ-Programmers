# 다이나믹 프로그래밍 알고리즘

import sys
input = sys.stdin.readline

def check_max(x, y):
    now = gold_mine[x][y]
    now_max = 0
    x_idx = x - 1
    while x_idx <= x + 1:   # 왼쪽 위부터 왼쪽 아래까지 비교할 수 있도록
        if x_idx >= 0 and x_idx < n:     # index값이 금광 안을 벗어나지 않도록
            now_max = max(now_max, gold_mine[x_idx][y-1] + now)
        x_idx += 1
    return now_max

def mine(gold_mine):
    # 세로 일자로 된 금광이면 비교할 필요가 없기 때문에 같은 라인의 최댓값 구하기
    if m == 1:
        return max([gold_mine[i][0] for i in range(n)])
    else:
        for j in range(1, m):
            for i in range(n):
                gold_mine[i][j] = check_max(i, j)       # 해당 위치의 가능한 최댓값으로 초기화
    return max([gold_mine[i][m - 1] for i in range(n)])    # 마지막 열의 최댓값

# def print_g():
#     for i in range(n):
#         print(gold_mine[i])        

T = int(input().rstrip())
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    golds = list(map(int, input().rstrip().split()))
    gold_mine = [golds[i:i+m] for i in range(0, n*m, m)]    # 금광 2차원 배열로 초기화
    # print_g()
    print(mine(gold_mine))
    # print_g()
    
# 풀이 : 더한 값을 누적하여 마지막 열에서 최댓값 선택