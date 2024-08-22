# 골드4 11054번
# https://www.acmicpc.net/problem/11054

N = int(input())
A = list(map(int, input().split()))

in_dp = [0 for _ in range(N)]
de_dp = [0 for _ in range(N)]

# 증가 순열 dp
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            in_dp[i] = max(in_dp[i], in_dp[j] + 1)

# 감소 순열 dp
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            de_dp[i] = max(de_dp[i], de_dp[j] + 1)

print(max([in_dp[i] + de_dp[i] for i in range(N)])+1)