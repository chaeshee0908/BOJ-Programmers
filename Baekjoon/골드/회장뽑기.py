# https://www.acmicpc.net/problem/2660
# 플로이드 워셜 골드 5

import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
group = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            group[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    group[a][b] = 1
    group[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            group[a][b] = min(group[a][b], group[a][k] + group[k][b])

score = []
p_score = INF
for person in group:
    s = max(person[1:])
    if p_score > s:
        p_score = s
    score.append(s)
print(p_score, score.count(p_score))
for i in range(1, N + 1):
    if score[i] == p_score:
        print(i, end=' ')