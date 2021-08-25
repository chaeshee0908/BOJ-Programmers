n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
for d in data:
    print(d, end= ' ')