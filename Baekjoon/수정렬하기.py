# 구현, 정렬

num = int(input())
data = []
for _ in range(num):
    n = int(input())
    data.append(n)
data.sort()
for i in range(num):
    print(data[i])
    