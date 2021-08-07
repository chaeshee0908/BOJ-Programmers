# 4153번 (브론즈3)
# 수학, 기하학

answer = []
while True:
    triangle = list(map(int,input().split()))
    if sum(triangle) == 0:
        break
    triangle.sort()
    if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
        answer.append('right')
    else:
        answer.append('wrong')
print('\n'.join(answer))