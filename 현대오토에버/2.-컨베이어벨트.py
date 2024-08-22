from collections import deque

needs = [0] + list(map(int, input().split()))   # 필요 부품 수
N = int(input())    # 컨베이어 벨트 위의 부품 수
belt = list(map(int, input().split()))  # 컨베이어 벨트에 올라가 있는 부품의 목록
result = 100

for i in range(N):
    now_belt = belt[i:] + belt[:i]  # 벨트 시작위치 변경
    now_needs = needs.copy()
    cnt = 0 # 확인해야 하는 부품 수
    # 새로운 시작점마다 확인 부품 개수 세기
    for j in range(N):
        # 필요 부품 모두 찾은 경우
        if sum(now_needs) == 0:
            break
        # 확인한 부품이 필요한 부품일 때
        now_needs[now_belt[j]] = max(0, now_needs[now_belt[j]]-1)
        cnt += 1
    # 필요한 부품을 전부 얻기 불가능
    if cnt == N and sum(now_needs) != 0:
        result = -1
        break
    # 확인 부품 개수
    else:
        result = min(result, cnt)
print(result)
    