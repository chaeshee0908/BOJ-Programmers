# 골드5 13398번
# https://www.acmicpc.net/problem/13398

INF = int(1e9)

n = int(input())
numbers = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = numbers[0]
dp[0][1] = numbers[0]

for i in range(1, n):
    # 숫자를 제외하지 않을 경우
    dp[i][0] = max(dp[i-1][0] + numbers[i], numbers[i])
    # 하나의 숫자를 제외할 경우
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + numbers[i])
                                                                                                                                                                                                                                               
result = -INF
for d in dp:
    result = max(result, max(d))
print(result)
