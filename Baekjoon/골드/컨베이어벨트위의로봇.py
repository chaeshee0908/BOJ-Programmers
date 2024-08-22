from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
belt_info = deque([[x, 0] for x in belt])

def first():
    belt_info.appendleft(belt_info.pop())
    if belt_info[N-1][1] == 1:  # 로봇이 내리는 위치에 있을 때
        belt_info[N-1][1] = 0   # 로봇 내림

def second():
    for i in range(N-2, -1, -1):
        robot = belt_info[i][1]
        # 현 위치에 로봇이 있고 이동 가능할 때(다음 칸에 로봇이 없고, 내구도가 0이 아닐 때)
        if robot == 1 and belt_info[i+1][0] != 0 and belt_info[i+1][1] == 0:
            belt_info[i+1][0] -= 1  # 이동 시 내구도 감소
            belt_info[i+1][1] = 1   # 로봇 이동
            belt_info[i][1] = 0     # 현위치의 로봇 이동
    if belt_info[N-1][1] == 1:  # 로봇이 내리는 위치에 있을 때
        belt_info[N-1][1] = 0   # 로봇 내림
            
def third():
    now_durability = belt_info[0][0]
    if now_durability != 0:
        belt_info[0][0] -= 1    # 내구도 감소
        belt_info[0][1] = 1     # 로봇 올라감

def check_belt():
    zero_num = 0
    for b in belt_info:
        if b[0] == 0:
            zero_num += 1
    if zero_num >= K:
        return False
    else:
        return True

availability = True
count = 0
while availability:
    count += 1
    first()
    second()
    third()
    availability = check_belt()

print(count)
    
    
