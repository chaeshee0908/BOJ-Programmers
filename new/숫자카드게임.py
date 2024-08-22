N, M = map(int, input().split())
min_values = []
for _ in range(N):
    card = list(map(int, input().split()))
    min_values.append(min(card))

print(max(min_values))