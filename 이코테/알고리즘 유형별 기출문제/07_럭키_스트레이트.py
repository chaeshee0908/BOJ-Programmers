# 구현 알고리즘
# 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"를 출력
num = list(input())
m = len(num)//2
n1 = num[:m]
n2 = num[m:]
left, right = 0, 0
for i in range(m):
    left += int(n1[i])
    right += int(n2[i])
if left == right:
    print('LUCKY')
else:
    print('READY')