# 그리디 알고리즘
# 각 줄의 카드들 중 가장 최솟값들 중의 최댓값 구하기

N,M = map(int,input().split())
min_list = [0]*3
for i in range(N):
    cards = list(map(int,input().split()))
    min_list[i] = min(cards)
print(max(min_list))