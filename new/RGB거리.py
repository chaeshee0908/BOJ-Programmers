# dp

# 비용, 색상
dp = [[0, -1]] * 1001
N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

from itertools import permutations

def find_min_group(n, value):
    rgb = [0, 1, 2]
    group = list(permutations(rgb, 2))
    min_value = 2000
    # 앞 뒤 집의 비용 합이 최소인 경우 구하기
    for f, b in group:
        if min_value > cost[n-1][f] + cost[n][b]:
            min_value = cost[n-1][f] + cost[n][b]
            f_color, b_color = f, b
    # dp[n]값, 색상
    return (value + min_value, b)

def find_min_value(n, value):
    color = dp[n-1][1]
    min_value = 1000
    for i in range(3):
        if color == i:
            continue
        if min_value > cost[n][i]:
            min_value = cost[n][i]
            now_color = i
    # dp[n]값, 색상
    return (value + min_value, i)
    

# 초기화
dp[0][0], dp[0][1] = cost[0][0], 0
# 색상 for문
for i in range(3):
    # dp 저장 값 보다 현재 값이 더 작을 때
    if cost[0][i] < dp[0][0]:
        dp[0][0] = cost[0][i]
        dp[0][1] = i
dp[1][0], dp[1][1] = find_min_value(1, dp[0][0])

for i in range(2, N):
    