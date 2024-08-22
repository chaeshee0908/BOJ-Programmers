# https://www.acmicpc.net/problem/1010
# 다이나믹 프로그래밍 실버 5

import sys
input = sys.stdin.readline

T = int(input())

# factorial값 저장 dp 테이블
d = [1] * 30
d[1] = 1
for i in range(2, 30):
    d[i] = d[i - 1] * i

for _ in range(T):
    n, m = map(int, input().split())
    # 점화식 : mCn -> m!/((m-n)!*n!)
    answer = d[m] // (d[m-n] * d[n])
    print(answer)