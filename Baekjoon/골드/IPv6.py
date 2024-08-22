# 골드5 3107번
# https://www.acmicpc.net/problem/3107

split_ip = input().split(':')

# 규칙 1
for i in range(len(split_ip)):
    # ::으로 축약된 경우가 아니고, 축약되어있는 경우
    if split_ip[i] != '' and len(split_ip[i]) != 4:
        # 0을 추가해 원상태로 복구
        split_ip[i] = '0' * (4 - len(split_ip[i])) + split_ip[i]

# 규칙 2(해당하는 경우에만)
# 0으로만 이루어진 형태가 ::으로 축약된 경우 있는지 확인
num = 0 # 축약되지 않은 부분의 개수
if '' in split_ip:
    for i in range(len(split_ip)):
        if split_ip[i] != '':
            num += 1
        else:
            idx = i # 규칙2가 사용된 위치
    split_ip[idx] = '0000' * (8 - num)
    
ip = ''.join(split_ip)
answer = ''
for i in range(0, len(ip), 4):
    answer += ip[i:i+4]
    # 마지막에만 : 안 붙임
    if i != 28:
        answer += ':'
print(answer)
            
    