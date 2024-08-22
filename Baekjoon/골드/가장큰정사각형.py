# https://www.acmicpc.net/problem/1915
# 다이나믹 프로그래밍 골드 4

# 한번에 숫자 리스트로 입력받기
# list(map(int, list(input())))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
max_len = 0
array = []
for _ in range(n):
    array.append(list(input()))

# 각 위치에 대한 가능한 최대의 정사각형 한 변의 길이 dp 테이블
d = [[0] * m for _ in range(n)]

# n, m 둘 중 하나라도 1인 경우 
if n == 1 or m == 1:
    for i in range(n):
        # 1이 하나라도 있다면 최대 정사각형 크기는 1
        if '1' in array[i]:
            print(1)
            exit(0)
    print(0)
    exit(0)

# 1로 표시되어 있는 곳 dp 테이블에 1로 초기화
for i in range(n):
    for j in range(m):
        if array[i][j] == '1':
            d[i][j] = 1


for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and array[i][j] == '1':
            d[i][j] += min(d[i][j-1], d[i-1][j], d[i-1][j-1])
        max_len = max(max_len, d[i][j])

print('---------------------')
for i in range(n):
    print(d[i])
print('---------------------')
print(max_len*max_len)