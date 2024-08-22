# from collections import deque
# from itertools import combinations

# def is_eight_graph(route, connection_node):
#     for c in connection_node:
#         if c in route:
#             return True
#     return False

# def is_stick_graph(route, graph):
#     start = route[0]
#     new_route = []
#     q = deque([])
#     q.append(start)
#     print('gg',route, graph)
#     while q:
#         node = q.popleft
#         new_route.append(node)
#         for v in graph[node]:
#             q.append(v)
#     if route == new_route:
#         return True
#     return False
        

# def order_nodes(graph, node_in, num):
#     node_order = deque([])
#     print(node_in)
#     while len(node_order) < num:
#         node_in = dict(sorted(node_in.items(), key = lambda item: item[1]))
#         print(node_in)
#         node = list(node_in.keys())[0]
#         print(node)
#         node_order.append(node)
#         print(graph)
#         for v in graph[node]:
#             print('연결된 노드:', v)
#             if v in node_in.keys():
#                 node_in[v] -= 1
#         del node_in[node]
#     return node_order 

# def solution(edges):
#     all_edges = [item for edge in edges for item in edge]
#     nodes = list(set(all_edges))
#     num = len(nodes)
#     graph = [[] for _ in range(num + 1)]
#     node_in = {}    # 해당 노드로 들어오는 간선 개수 
#     for n in nodes:
#         node_in[n] = 0
#     for edge in edges:
#         u, v = edge[0], edge[1]
#         graph[u].append(v)
#         node_in[v] += 1
    
#     # 새로운 노드 찾기
#     for n in node_in.keys():
#         if node_in[n] == 0 and len(graph[n]) > 1:
#             new_node = n
    
#     node_order = order_nodes(graph, node_in, num)
#     print(node_order)
    
#     donut, stick, eight = 0, 0, 0
#     connection_node = []

#     # 8자 그래프 개수 세기
#     for i in range(1, num + 1):
#         if len(graph[i]) == 2 and i != new_node:
#             connection_node.append(i)
#             eight += 1
    
#     route = []
#     while node_order:
#         node = node_order.popleft()
#         if node == new_node:
#             continue
#         if node in graph[new_node]:
#             # 8자 그래프일 때 무시
#             if is_eight_graph(route, connection_node):
#                 pass
#             if is_stick_graph(route, graph):
#                 stick += 1
#             else:
#                 donut += 1 
#             route = [node]
#         else:
#             route.append(node)
    
#     # 8자 그래프일 때 무시
#         if is_eight_graph(route, connection_node):
#             pass
#         if is_stick_graph(route, graph):
#             stick += 1
#         else:
#             donut += 1      
    
#     return [new_node, donut, stick, eight]



from collections import deque
import sys
sys.setrecursionlimit(1000001)

node, edge = 0, 0

def dfs(graph, visited, num):
    global node
    global edge

    visited[num] = 1
    node += 1
    for x in graph[num]:
        edge += 1
        if visited[x] == 0:
            dfs(graph, visited, x)

def solution(edges):
    global node
    global edge

    all_edges = [item for edge in edges for item in edge]
    nodes = list(set(all_edges))
    num = len(nodes)
    graph = [[] for _ in range(num + 1)]
    visited = [0 for _ in range(num + 1)]

    node_degree = [-1 for _ in range(num+1)]
    donut, stick, eight = 0, 0, 0
    for a, b in edges:
        graph[a].append(b)
        node_degree[a] = max(node_degree[a], 0)
        node_degree[b] = max(node_degree[b], 0)
        node_degree[b] += 1
    
    q = deque()
    for i in range(num+1):
        if node_degree[i] == 0:
            q.append(i)
    for x in q:
        if len(graph[x]) > 1:
            start_node = x
            break
    
    for x in graph[start_node]:
        dfs(graph, visited, x)
        # 도넛일 때 (간선 개수와 노드 개수 같음)
        if node == edge:
            donut += 1
        # 막대일 때 (간선 개수보다 노드 개수가 하나 더 많음)
        elif node-1 == edge:
            stick += 1
        # 8자일 때 (노드 개수보다 간선 개수가 하나 더 많음)
        elif node+1 == edge:
            eight += 1
        node, edge = 0, 0

    return [start_node, donut, stick, eight]


case1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
case2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(case2))