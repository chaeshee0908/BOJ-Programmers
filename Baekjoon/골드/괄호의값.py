# 골드5 2504번
# https://www.acmicpc.net/problem/2504

bracket = list(input())
stack = []
tmp = 1
answer = 0

for i in range(len(bracket)):
    b = bracket[i]
    # 괄호 열기
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)
    # 괄호 닫기
    elif b == ')':
        # 올바른 괄호가 아닐 때
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if bracket[i-1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
    elif b == ']':
        # 올바른 괄호가 아닐 때
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if bracket[i-1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

print(answer)
