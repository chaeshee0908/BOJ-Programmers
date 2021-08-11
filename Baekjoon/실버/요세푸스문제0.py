# 11866번 (실버4)
# 자료구조 큐

from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])
result = []
idx = k-1
while queue:
    # 없애야하는 인덱스 이전 값들을 다 큐 뒤에 연결
    for i in range(idx):
        queue.append(queue.popleft())
    # 없애야 하는 인덱스가 제일 앞순서로 왔으므로 pop 해줌
    result.append(queue.popleft())
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(f'{result[-1]}>')