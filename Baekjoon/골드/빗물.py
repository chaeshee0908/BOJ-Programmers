# 골드5 14719번
# https://www.acmicpc.net/problem/14719

h, w = map(int, input().split())
block = list(map(int, input().split()))
puddle = []
start = 0   # 시작 인덱스

while start <= w:
    now_h = block[start]   # 현재 위치 블록 높이
    next_h = []     # 뒤에 오는 블록 높이들
    next_idx = []   # 뒤에 오는 블록 위치 인덱스
    now_d = start   # 현재 위치 인덱스
    for i in range(start + 1, w):
        next_h.append(block[i])
        next_idx.append(i)
        if block[i] >= now_h:
            break
    # 현재 이후에 더 쌓인 블록이 없다면 while문 나감
    if not next_h or sum(next_h) == 0:
        break
    # 현재 이후에 비가 쌓일 수 없는 경우일 때 (다음 남은 블록이 하나일 떄)
    if len(next_h) == 1:
        start += 1
        continue
    # 더 높은 블록이 나오지 않았으면 낮은 블록 중 가장 높은 블록 높이까지 비 고임
    rain_h = max(next_h[1:])
    puddle_h = min(now_h, rain_h)
    rain = 0
    for i, h in enumerate(next_h):
        # 빗물이 고일 수 있는 최대 높이가 되면 멈춤
        if h == rain_h:
            start = next_idx[i]
            break
        if puddle_h > h:
            rain += puddle_h - h
    if rain == 0:
        break
    puddle.append(rain)

# 고일 수 있는 빗물이 없을 때
if not puddle:
    print(0)
else:
    print(sum(puddle))