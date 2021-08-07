# 10250번 (브론즈3)
# 수학, 구현, 사칙연산

n = int(input())
room = []
for _ in range(n):
    H, W, N = map(int, input().split())
    y = H if N % H == 0 else N % H
    x = N // H if N % H == 0 else N // H + 1
    if x < 10:
        x = '0' + str(x)
    r = str(y) + str(x)
    room.append(r)
print('\n'.join(room))