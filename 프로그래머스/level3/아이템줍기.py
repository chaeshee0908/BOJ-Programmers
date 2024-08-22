# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque
ground = [[0] * 102 for i in range(102)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 캐릭터, 아이템 좌표 2배로 늘리기
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2

    # 좌표 직사각형 표시
    for r in rectangle:
        # 좌표를 2배로 늘리기
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형 내부 2로 채우기
                if x1 < i < x2 and y1 < j < y2:
                    ground[i][j] = 2
                # 테두리 1로 채우기
                elif ground[i][j] != 2:
                    ground[i][j] = 1 

    q = deque([(cx, cy)])
    distance = [[1] * 102 for i in range(102)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖으로 나갈 시 재탐색
            if nx < 0 or nx > 101 or ny < 0 or ny > 101:
                continue
            # 테두리에 포함되면서 방문 안 했을 경우
            if ground[nx][ny] == 1 and distance[nx][ny] == 1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny)) 

    return distance[ix][iy] // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
# print(solution([[1,1,5,7]], 1, 1, 4, 7))
# # print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
# print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))