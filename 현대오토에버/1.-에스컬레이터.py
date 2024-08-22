from collections import deque

N = int(input())
board = [[0, 0, 0]] # 시작 라인 설정
for _ in range(N):
    board.append(list(map(int, input().split())))

distance = [[0]*3 for _ in range(N+1)]  # 칸 이동 거리

q = deque([])
q.append((0, 1))    # 가운데 칸에서 시작
# 이동 범위
dx = [1, 1, 1, 1, 1]    # 무조건 아래로 내려감
dy = [-2, -1, 0, 1, 2]  # 좌우 이동(최대 2칸)

while q:
    x, y = q.popleft()
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 들어오지 않으면 패스
        if nx < 0 or nx > N or ny < 0 or ny >= 3:
            continue
        # 빈 칸이어야함
        if board[nx][ny] == 0:
            # 이동한 칸의 개수 더하기
            if distance[nx][ny] == 0:
                distance[nx][ny] = abs(ny-y) + distance[x][y]
            else:
                distance[nx][ny] = min(distance[nx][ny], abs(ny-y) + distance[x][y])
            q.append((nx, ny))

end = distance[-1]
end_list = []
for cnt in end:
    # 도달 가능한 부분만 확인
    if cnt != 0:
        end_list.append(cnt)

# 최소 이동거리 출력
print(min(end_list))
