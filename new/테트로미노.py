import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

# 폴리오미노로 표현 가능한 모든 19가지 경우의 수
poly = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],   # I자 
    [(0, 0), (0, 1), (0, 2), (0, 3)],   # I자 
    [(0, 0), (0, 1), (1, 0), (1, 1)],   # 정사각형
    [(0, 0), (1, 0), (2, 0), (2, 1)],   # L자
    [(0, 0), (0, 1), (0, 2), (1, 0)],   # L자
    [(0, 0), (0, 1), (1, 1), (2, 1)],   # L자
    [(0, 0), (0, 1), (0, 2), (-1, 2)],  # L자
    [(0, 0), (0, 1), (-1, 1), (-2, 1)], # L자
    [(0, 0), (0, 1), (0, 2), (1, 2)],   # L자
    [(0, 0), (0, 1), (1, 0), (2, 0)],   # L자
    [(0, 0), (1, 0), (1, 1), (1, 2)],   # L자
    [(0, 0), (1, 0), (1, 1), (2, 1)],   # 번개
    [(0, 0), (0, 1), (-1, 1), (-1, 2)], # 번개
    [(0, 0), (0, 1), (-1, 1), (1, 0)],  # 번개
    [(0, 0), (0, 1), (1, 1), (1, 2)],   # 번개
    [(0, 0), (0, 1), (1, 1), (0, 2)],   # ㅜ
    [(0, 0), (-1, 1), (0, 1), (1, 1)],  # ㅓ
    [(0, 0), (0, 1), (0, 2), (-1, 1)],  # ㅗ
    [(0, 0), (-1, 0), (0, 1), (1, 0)]   # ㅏ
]

result = 0

def isAvailable(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

for x in range(N):
    for y in range(M):
        for p1, p2, p3, p4 in poly:
            px1, py1 = p1
            px2, py2 = p2
            px3, py3 = p3
            px4, py4 = p4
            nx1, ny1, nx2, ny2, nx3, ny3, nx4, ny4 = x+px1, y+py1, x+px2, y+py2, x+px3, y+py3, x+px4, y+py4
            total = 0
            # 종이 안에 폴리오미노가 들어올 때 
            if isAvailable(nx1, ny1) and isAvailable(nx2, ny2) and isAvailable(nx3, ny3) and isAvailable(nx4, ny4):
                total = paper[nx1][ny1] + paper[nx2][ny2] + paper[nx3][ny3] + paper[nx4][ny4]
                result = max(result, total)

print(result)