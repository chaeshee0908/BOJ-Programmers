# 골드4 9935번
# https://www.acmicpc.net/problem/9935

now = input()
bomb = input()
stack = []

for s in now:
    stack.append(s)
    if s == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')