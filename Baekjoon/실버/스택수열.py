# 1874번 (실버3)
# 자료구조, 스택

실패!!

from collections import deque

def make_seq(n_list, n):
    global seq
    stack = []
    ret = []
    n_list = deque(n_list)
    cor = []
    num = 2
    stack.append(1)
    ret.append('+')
    while n_list:
        value = n_list.popleft()
        while True:
            if num > n + 1:
                return []
            if stack and stack[-1] == value:
                cor.append(stack.pop())
                ret.append('-')
                break
            elif stack and stack[-1] != value:
                stack.append(num)
                ret.append('+')
                num += 1
            else:
                break
    if cor == seq:
        return ret
    else:
        return []

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
seq = n_list
if make_seq(n_list, n) == []:
    print('NO')
else:
    print('\n'.join(make_seq(n_list, n)))
