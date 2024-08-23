# dp문제

N = int(input())
dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    if dp[i-3] < 0 and dp[i-5] < 0:
        continue
    if dp[i-3] < 0 or dp[i-5] < 0:
        dp[i] = 1 + max(dp[i-3], dp[i-5])
    else:
        dp[i] = 1 + min(dp[i-3], dp[i-5])

print(dp[N])
    