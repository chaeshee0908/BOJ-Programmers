# 2606번 (실버3)
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [False] * n

matrix = [[0] * (n+1) for _ in range(n+1)]
print(matrix)
for v in graph:
    if len(v) == 1:
        continue
    a, b = tuple(v)
    matrix[a][b] = 1
    matrix[b][a] = 1
    for i in range(n+1):
        print(matrix[i])

# for i in range(1, n+1):
#     matrix[i][i] = 0
        
for i in range(n+1):
    print(matrix[i])

# def bfs(graph, start, visited):
#     result = 0
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in range()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 print(queue)
#                 visited[i] = True
#                 result += 1 
#     return result

# print(bfs(graph, 1, visited))
