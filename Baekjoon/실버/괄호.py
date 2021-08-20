# 9012번 (실버4)
# 자료구조, 문자열, 스택

from collections import deque

def check_VPS(datas):
    datas = deque(datas)
    stack = []
    while datas:
        if datas[0] == '(':
            stack.append(datas[0])
        if datas[0] == ')':
            if len(stack):
                stack.pop()
            else:
                return False
        datas.popleft()
    if len(stack) == 0:
        return True
    else:
        return False

n = int(input())
ans = []
for _ in range(n):
    str = input().rstrip()
    datas = list(str)
    if check_VPS(datas):
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))
