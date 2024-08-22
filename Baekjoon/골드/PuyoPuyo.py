# 골드 4 11559번
# https://www.acmicpc.net/problem/11559

board = []
for _ in range(12):
    board.append(list(input()))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 연결된 뿌요 찾기
def check_link(x, y, puyo):
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    link = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == puyo:
                visited[nx][ny] = True
                q.append((nx, ny))
                link.append((nx, ny))
    return link

# 뿌요 터뜨리기
def pops(link_puyo):
    for l in link_puyo:
        x, y = l
        board[x][y] = '.'

# 터뜨린 후 내리기
def pull_down():
    for i in range(6):
        line = ''
        for j in range(12):
            line += board[j][i]
        line = line.replace('.', '')
        line_array = list('.' * (12-len(line)) + line)
        for a in range(12):
            board[a][i] = line_array[a]
    

chain = 0
while True:
    pop_availability = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            # 방문하지 않고 뿌요가 있을 때 
            if not visited[i][j] and board[i][j] != '.':
                link_puyo = check_link(i, j, board[i][j])
                if len(link_puyo) >= 4:
                    pops(link_puyo)
                    pop_availability = True
    if pop_availability == True:
        pull_down()
        pop_availability = False
        chain += 1
    else:
        break

print(chain)
                