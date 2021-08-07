# 2309번 (브론즈2)
# 브루트포스 알고리즘

height = []
for _ in range(9):
    height.append(int(input()))
s = sum(height)
two = s - 100
check = 0
for i in range(8):
    for j in range(9):
        if i == j:
            continue
        if height[i] + height[j] == two:
            check = 1
            x, y = height[i], height[j]
            break
    if check == 1:
        break
height.remove(x)
height.remove(y)
height.sort()
for i in range(7):
    print(height[i])