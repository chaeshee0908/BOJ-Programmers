# https://www.acmicpc.net/problem/11724
# bfs/dfs 실버2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def dfs(graph, now, visited):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(graph, i, visited)

num = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        num += 1
print(num)        