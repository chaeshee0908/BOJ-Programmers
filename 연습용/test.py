from collections import deque

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
    m, v = map(int, input().split())
    jewel.append([m, v])
for _ in range(K):
    c = int(input())
    bag.append(c)

jewel = deque(jewel)
jewel.sort(key=lambda x: (x[1], x[0]))
bag.sort(reverse=True)

for b in bag:
    now_jewel = jewel[0]
    while b < now_jewel[0]:
        now_jewel.popleft()


    