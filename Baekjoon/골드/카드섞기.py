# 골듣4 1091번
# https://www.acmicpc.net/problem/1091

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
result = 0
fail = False

# 카드 위치, 카드 숫자
origin_cards = [[i, i] for i in range(N)]
cards = origin_cards.copy()

# 목적 달성했는지 확인
def success():
    # 카드 위치 = P[i], 카드 숫자 = i
    sorted_cards = sorted(cards, key=lambda x: x[1])
    for i in range(N):
        location, num = sorted_cards[i]
        if location % 3 != P[i]:
            return False
    return True

# 카드 섞기
def shuffle_cards():
    global result
    for i in range(N):
        cards[i][0] = S[i]
    result += 1
    cards.sort(key=lambda x: x[0])

# 불가능한지
def check_fail():
    # 카드가 섞기 전으로 돌아왔는데도 성공하지 못하면 불가능 
    for i in range(N):
        ol, on = origin_cards[i]
        cl, cn = cards[i]
        if ol != cl or on != cn:
            return False
    return True

while True:
    if success():
        break
    shuffle_cards()
    if check_fail():
        fail = True
        break

if fail:
    print(-1)
else:
    print(result)
