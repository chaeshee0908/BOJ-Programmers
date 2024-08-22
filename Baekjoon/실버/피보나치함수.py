# 1003번 (실버3)
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

def fibonacci(n):
    global zero
    global one

    if d[n] != 0:
        return d[n]
    elif n == 0:
        return 0
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2)
        zero[n] = zero[n-1] + zero[n-2]
        one[n] = one[n-1] + one[n-2]
        return d[n]

times = int(input())
d = [0] * 41
zero = [0] * 41
one = [0] * 41
zero[0], one[1], d[1] = 1, 1, 1
answer = []
for _ in range(times):
    n = int(input())
    fibonacci(n)
    answer.append([zero[n], one[n]])
for a in answer:
    print(a[0], a[1])