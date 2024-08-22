N, M = map(int, input().split())
A, B, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
board[A][B] = 2

count = 1

# 북, 동, 남, 서 
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    check = 0
    for i in range(4):
        # 왼쪽방향으로 회전
        d -= 1
        if d == -1:
            d = 3
        check += 1
        dx, dy = move[d]
        nx = dx + A
        ny = dy + B 
        # 이동 가능한 칸일때 
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:    
            board[nx][ny] = 2
            count += 1
            A, B = nx, ny
            break
    # 모두 체크했지만 갈 곳이 없을 경우
    if check == 4:
        dx, dy = move[d]
        # 바라보는 방향 뒤 이동
        nx = A - dx
        ny = B - dy
        # 방향 유지한채 뒤로 갈 수 있는 경우(뒤가 바다가 아닌 경우)
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1:
            A, B = nx, ny
        # 더 이상 이동 불가능 
        else:
            break

print(count)
        