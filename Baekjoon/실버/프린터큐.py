# 1966번 (실버3)
# 구현, 자료구조, 시뮬레이션, 큐

from collections import deque
import sys

def solution(priorities, location, n):
    queue = deque(priorities)
    data = ['N'] * n
    data[location] = 'Y'
    datas = deque(data)
    cnt = 1
    while queue:
        if datas[0] == 'Y' and queue[0] == max(queue):
            break
        if queue[0] < max(queue):
            queue.append(queue.popleft())
            datas.append(datas.popleft())
        else:
            cnt += 1
            queue.popleft()
            datas.popleft()
    return cnt 

case = int(input())
ans = []
for _ in range(case):
    n, location = map(int, sys.stdin.readline().rstrip().split())
    priorities = list(map(int, sys.stdin.readline().rstrip().split()))
    ans.append(solution(priorities,location, n))
for a in ans:
    print(a)