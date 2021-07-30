# 구현

def move(place, move, N):
    if move == 'R':
        if place[1] < N:
            place[1] += 1
    elif move == 'L':
        if place[1] > 1:
            place[1] -= 1
    elif move == 'U':
        if place[0] > 1:
            place[0] -= 1
    elif move == 'D':
        if place[0] < N:
            place[0] += 1

N = int(input())
plans = list(input().split())
place = [1,1]
for plan in plans:
    move(place, plan, N)
print(place[0], place[1])