# 정렬

n = int(input())
datas = []
for _ in range(n):
    year, name = input().split()
    datas.append([int(year), name])
# 나이 기준으로 정렬(이름은 정렬되지 않는다)
datas.sort(key=lambda x: x[0])
for data in datas:
    print('{} {}'.format(data[0], data[1]))