from itertools import combinations

N = int(input())
numbers = list(map(int, input().split()))
check = [0] * 2000001

for i in range(1, N+1):
    for c in combinations(numbers, i):
        value = sum(c)
        check[value] = 1

for idx in range(1, 2000001):
    if check[idx] == 0:
        print(idx)
        break