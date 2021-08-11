# 1021번 (실버4)
# 자료구조, 덱

from collections import deque

n, m = map(int, input().split())
places = list(map(int, input().split()))
queue = deque(i for i in range(1,n+1))
cnt = 0
for place in places:
    # 뽑고자 하는 수가 제일 앞에 도달할 때 까지 반복
    while queue[0] != place:
        # 뽑고자 하는 위치가 왼쪽으로 이동시키는 것이 더 가까울 때
        if queue.index(place) <= len(queue)//2:
            queue.append(queue.popleft())
        # 뽑고자 하는 위치가 오른쪽으로 이동시키는 것이 더 가까울 때
        else:
            queue.appendleft(queue.pop())
        # 반복문 내의 움직임은 2,3번 이므로 카운트
        cnt += 1
    queue.popleft()
print(cnt)