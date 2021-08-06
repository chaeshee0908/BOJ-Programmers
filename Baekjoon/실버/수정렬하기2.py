# 정렬
# pypy3

num = int(input())
datas = []
for _ in range(num):
    n = int(input())
    datas.append(n)
datas.sort()
for data in datas:
    print(data)