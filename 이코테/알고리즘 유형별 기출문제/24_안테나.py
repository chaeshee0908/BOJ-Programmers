# 정렬 알고리즘
# 2019 SW 마에스트로 입학 테스트
# 링크 : https://www.acmicpc.net/problem/18310

def total_distance(num, houses):
    distance = 0
    for h in houses:
        distance += abs(h - num)
    return (num, distance)

import sys
input = sys.stdin.readline

N = int(input().rstrip())
houses = list(map(int, input().rstrip().split()))
houses.sort()
if N == 1:
    print(houses[0])
else: 
    idx = len(houses) // 2
    T = [total_distance(houses[idx-1], houses), total_distance(houses[idx], houses)]
    L = sorted(T, key=lambda x : (x[1], x[0]))
    print(L[0][0])