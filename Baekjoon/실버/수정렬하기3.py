# 정렬
# 계수정렬

import sys

n = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(n):
    input_data = int(sys.stdin.readline())
    count[input_data] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)