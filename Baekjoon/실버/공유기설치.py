# 2110번 (실버1)
# 이분 탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
houses = []
for _ in range(n):
    houses.append(int(input().rstrip()))
houses.sort()
start = 1
end = houses[-1] - houses[0]

while start <= end:
    # mid는 공유기 사이의 간격의 최솟값
    mid = (start + end) // 2
    gong = 1
    # 이전 집과의 거리 측정을 위한 이전 집 좌표
    pre_house = houses[0]
    for x in houses:
        d = x - pre_house   # 공유기 간격
        # 공유기 간격이 최소값(mid)보다 크거나 같을 때 공유기 설치
        if mid <= d:
            gong += 1
            pre_house = x
    # 설치한 공유기 개수가 주어진 공유기 개수보다 많을 때 : 간격을 늘려준다(공유기 개수 줄이기)
    if gong >= c:
        result = mid
        start = mid + 1
    # 설치한 공유기 개수가 주어진 공유기 개수보다 적을 때 : 간격을 좁혀준다(공유기 개수 늘리기) 
    else:
        end = mid - 1            

print(result)