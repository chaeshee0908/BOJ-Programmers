N = int(input())
score = list(map(int, input().split()))
perc, minA = map(int, input().split())

score.sort(reverse=True)
s_num = N * perc // 100
j_num = 0
for s in score:
    if s >= minA:
        j_num += 1
print("{} {}".format(s_num, j_num))