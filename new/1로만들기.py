# dp 문제

N = int(input())
dp = [0] * 1000001

for i in range(2, N+1):
    # 1 더하기
    dp[i] = dp[i-1] + 1
    # 2 곱하기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3 곱하기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N]) 