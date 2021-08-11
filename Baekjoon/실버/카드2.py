# 2164번 (실버4)
# 자료구조 큐

from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])