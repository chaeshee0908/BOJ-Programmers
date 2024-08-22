# 그리디 알고리즘
# 여행을 떠날 수 있는 그룹 수의 최댓값
N = int(input())
adv = list(map(int, input().split()))

adv.sort(reverse=True)
g, i = 0, 0
while i < len(adv):
    i = i + adv[i]
    g += 1
print(g)
    