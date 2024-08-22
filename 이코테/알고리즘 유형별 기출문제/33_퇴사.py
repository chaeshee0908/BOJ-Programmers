# 다이나믹 프로그래밍 알고리즘
# 링크 : https://www.acmicpc.net/problem/14501

import sys
input = sys.stdin.readline

N = int(input().rstrip())
consult = []
for _ in range(N):
    consult.append(list(map(int, input().rstrip().split())))
b_array = [0] * N

def benefit(s_idx, money):
    # 현재 가리키는 상담이 없으면 종료
    if s_idx >= N:
        return
    day = consult[s_idx][0]
    # 현재 가리키는 상담이 퇴사 전에 끝나지 않으면 종료
    if s_idx + day > N:
        return
    print('상담 기간 : {}, 상담 머니 합계 이전 돈 : {}'.format(day, money))
    money += consult[s_idx][1]
    print('{}일차 시작 돈 : {}, 상담 머니 : {}'.format(s_idx + 1, money, consult[s_idx][1]))
    print()
    if b_array[s_idx] < money:
        b_array[s_idx] = money
    for i in range(day):
        benefit(s_idx+day+i, money)

for d in range(consult[0][0]):
    money = 0
    benefit(d, money)
    print('--------------------------------------')

print(b_array)
print(max(b_array))