# https://www.acmicpc.net/problem/2644
# bfs/dfs 실버 2

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for person in family[v]:
           if not visited[person]:
                queue.append(person)
                visited[person] = True
                count[person] = count[v] + 1

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[] for _ in range(n + 1)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    family[p1].append(p2)
    family[p2].append(p1)
visited = [False] * (n + 1)
count = [0] * (n + 1)

bfs(a)

if count[b] != 0:
    print(count[b])
else:
    print(-1)
