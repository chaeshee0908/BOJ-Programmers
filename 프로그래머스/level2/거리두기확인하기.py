# bfs, dfs

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(room, x, y, d):
    visited = [[False]*5 for _ in range(5)]
    queue = deque()
    queue.append([x, y, d])
    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if room[nx][ny] == 'P':
                    if nd <= 2:
                        return False
                elif room[nx][ny] == 'O':
                    queue.append([nx, ny, nd])
    return True

def solution(places):
    answer = []
    for room in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if bfs(room, i, j, 0) == False:
                        flag = 0
        answer.append(flag)
    return answer

places = [["POOOP","OXXOX", "OPXPX", "OOXOX","POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
["OXPOO", "OPXOO", "OOOOO", "OOOOO", "OOOOO"],
["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]

print('answer :', solution(places))