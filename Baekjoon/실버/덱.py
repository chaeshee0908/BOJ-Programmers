# 10866번 (실버 4)
# 자료구조, 덱

from collections import deque
import sys

def execution(order):
    if 'push_back' in order:
        num = int(order.replace('push_back', ''))
        queue.append(num)
    elif 'push_front' in order:
        num = int(order.replace('push_front', ''))
        queue.appendleft(num)
    elif 'pop' in order:
        if queue:
            if order == 'pop_front':
                print(queue.popleft())
            else:
                print(queue.pop())
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