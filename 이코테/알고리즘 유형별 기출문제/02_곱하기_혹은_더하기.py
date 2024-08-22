# 그리디 알고리즘
# 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력
import sys
input = sys.stdin.readline
n = list(input().rstrip())
print(n)
n.sort()
if n[-1] == 0:
    print(0)
else:
    ans = 1
    for num in n:
        if int(num) != 0:
           ans *= int(num)
print(ans) 