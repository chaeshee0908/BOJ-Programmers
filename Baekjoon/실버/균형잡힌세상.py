# 4949번 (실버4)
# 자료구조, 문자열, 스택

from collections import deque

def check(datas):
    datas = deque(datas)
    stack = []
    for data in datas:
        if data == '(' or data == '[':
            stack.append(data)
        if data == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return False
        if data == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

ans = []
while True:
    str = input().rstrip()
    if str == '.':
        break
    datas = list(str)
    if check(datas):
        ans.append('yes')
    else:
        ans.append('no')

print('\n'.join(ans))    