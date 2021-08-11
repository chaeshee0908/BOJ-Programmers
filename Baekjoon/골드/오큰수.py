# 17298 (골드4)
# 자료구조, 스택

import sys
from collections import deque

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
NGE = ['-1']*n
stack = deque()
for i in range(n):
    # 스택에 값이 현재 비교 수보다 작으면 다 빼줌 
    while stack and seq[i] > seq[stack[-1]]:
        NGE[stack.pop()] = str(seq[i])
    # index() 함수를 사용하지 않기 위해(시간초과뜸) stack에 인덱스 값으로 넣어줌
    stack.append(i)
print(' '.join(NGE))