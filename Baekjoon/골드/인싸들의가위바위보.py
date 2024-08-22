# 골드3
# https://www.acmicpc.net/problem/16986

'''
지우가 이긴다 -> A[지우가 낸 손][상대방 손] = 2
(지우가 첫 순서이기 때문에 무승부로 이길 수는 없다.)
지우가 우승한다 -> 위의 경우가 K(승수)번 가장 먼저 일어나는 경우 
'''

from itertools import permutations
from collections import deque

# 손동작 수, 승수
N, K = map(int, input().split())
# 손동작
rsp = [i for i in range(N)]
# 상성 정보(2:이김, 1:비김, 0:짐)
comp_info = []
for _ in range(N):
    comp_info.append(list(map(int, input().split())))
# 경희 손동작 순서
kyunghee = list(map(int, input().split()))
# 민호 손동작 순서
minho = list(map(int, input().split()))
# 모든 플레이어 번호
player_numbers = [0, 1, 2]
score = [0, 0, 0]   # 지우, 경희, 민호

# 두 명이 가위바위보(0: 지우, 1: 경희, 2: 민호)
def play(p1, p2):
    global all_hands
    i = all_hands[p1].pop(0)    # 플레이어1의 손동작
    j = all_hands[p2].pop(0)    # 플레이어2의 손동작
    p3 = [x for x in player_numbers if x not in [p1, p2]]
    # p1이 p2를 이긴 경우
    if comp_info[i-1][j-1] == 2:
        winning_number[p1] += 1
        return (p1, p3[0])
    # p2가 p1을 이긴 경우
    elif comp_info[i-1][j-1] == 0:
        winning_number[p2] += 1
        return (p2, p3[0])
    # p1과 p2가 같은 손동작을 낸 경우
    else:
        # p1 승리
        if p1 > p2:
            winning_number[p1] += 1
            return (p1, p3[0])
        # p2 승리
        else:
            winning_number[p2] += 1
            return (p2, p3[0])

result = 0
# 모든 수를 내는 경우
for c in permutations(rsp, N):
    jiwoo = list(c) # 지우가 모두 다르게 내는 경우
    all_hands = [jiwoo, kyunghee.copy(), minho.copy()]    # 모든 플레이어의 손동작
    winning_number = [0, 0, 0]  # 지우, 경희, 민호
    round = 1
    next_p1, next_p2 = play(0, 1) # 1라운드
    # 지우가 낼 손동작이 남아있을 때까지(혹은 모두 낼 수 있을 때까지)
    while jiwoo and kyunghee and minho:
        # 우승자가 나왔을 때 
        if max(winning_number) == K:
            break
        round += 1
        next_p1, next_p2 = play(next_p1, next_p2)

    # 지우가 우승 가능할 때
    if winning_number[0] == K:
        result = 1
        break

print(result) 
        
