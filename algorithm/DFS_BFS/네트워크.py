# 프로그래머스
# Lv3
# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n)]
    # 컴퓨터 연결 정보 초기화
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 연결되어 있으면
            if computers[i][j] == 1:
                graph[i].append(j)
    visited = [False] * n
    network = [0] * n
    # 네트워크 넘버
    net_num = 1
    
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        network[start] = net_num
        while q:
            computer = q.popleft()
            for c in graph[computer]:
                if not visited[c]:
                    visited[c] = True
                    network[c] = net_num
                    q.append(c)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            # dfs를 돌고 나면 다른 네트워크를 사용하기 위해 번호 변경
            net_num += 1
    
    # 네트워크 번호 집합의 개수가 네트워크의 개수 (같은 네트워크 사용시 네트워크 번호 동일)
    result = set(network)
    return len(result)

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

                
    