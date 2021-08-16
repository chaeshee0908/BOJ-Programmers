from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    data = ['N'] * len(priorities)
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

p1 = [2,1,3,2]
p2 = [1,1,9,1,1,1]
print(solution(p1, 2))
print(solution(p2, 0))