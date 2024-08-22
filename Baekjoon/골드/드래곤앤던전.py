# 골드4 16434번
# https://www.acmicpc.net/problem/16434

N, ATK = map(int, input().split())
max_hp = 0
cur_hp = 0
for _ in range(N):
    t, a, h = map(int, input().split())
    # t=1: 몬스터
    if t == 1:
        if h % ATK == 0:
            cur_hp += - (h // ATK - 1) * a   # 몬스터 죽일 때 용사가 받는 피해량
        else:
            cur_hp += - (h // ATK) * a   # 몬스터 죽일 때 용사가 받는 피해량
    # t=2: 포션
    elif t == 2:
        ATK += a    # 공격력 증가
        max_hp = min(max_hp, cur_hp)    # 용사가 받은 피해량 중 가장 큰 값 저장
        cur_hp = cur_hp + h if cur_hp + h < 0 else 0    # 최대 hp까지만 생명력 충전
cur_hp = cur_hp * (-1) + 1
max_hp = max(max_hp * (-1) + 1, cur_hp)
print(max_hp)        
