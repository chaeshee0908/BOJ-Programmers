# 2579번 (실버3)
# 다이나믹 프로그래밍

from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
dp = deque()
dp.append(stair[0])
if n > 1:
    dp.append(stair[0] + stair[1])
if n > 2:
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))
for i in range(3, n):
    dp.append(max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3]))
print(dp.pop())