# https://www.acmicpc.net/problem/11052
# 다이나믹 프로그래밍 실버 1

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
# 금액의 최댓값 dp 테이블 
dp = [0] * (N + 1)
# 카드 한 개 살 때의 최댓값
dp[1] = P[1]

for i in range(2, N + 1):
    for k in range(i+1):
        dp[i] = max(P[k] + dp[i - k], dp[i])

print(dp[N])