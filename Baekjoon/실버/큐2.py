# 18258번 (실버4)
# 자료구조, 큐
# 시간초과 유의

from collections import deque
import sys

def execution(order):
    if 'push' in order:
        num = int(order.replace('push', ''))
        queue.append(num)
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
       
queue = deque()
orders = []
n = int(sys.stdin.readline())
for _ in range(n):
    o = sys.stdin.readline()
    orders.append(o.rstrip('\n'))
for order in orders:  
    execution(order)    