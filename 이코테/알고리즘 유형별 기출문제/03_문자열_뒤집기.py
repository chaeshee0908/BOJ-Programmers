# 그리디 알고리즘
# 다솜이가 해야하는 행동의 최소 횟수 출력
# 덩어리 개수를 세준다 

import sys
input = sys.stdin.readline
n = list(input().rstrip())
l = [0, 0]
for i in range(len(n)-1):
    if n[i] == '0' and n[i+1] == '1':
        l[0] += 1
    elif n[i] == '1' and n[i+1] == '0':
        l[1] += 1
print(l)
if sum(l) == max(l):
    print(max(l))
else:
    print(min(l))