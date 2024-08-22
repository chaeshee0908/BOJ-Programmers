# 골드5 1756번
# https://www.acmicpc.net/problem/1756

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

dist = 0
# 내려갈 때 더 크기가 커지는 오븐 줄이기
for i in range(D-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

idx = D
for p in pizza:
    while idx >= 0:
        idx -= 1
        # 들어갈 수 있는 크기의 도우
        if p <= oven[idx]:
            break

print(idx + 1)