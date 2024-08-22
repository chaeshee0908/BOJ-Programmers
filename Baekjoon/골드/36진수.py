# 골드1 1036번
# https://www.acmicpc.net/problem/1036

N = int(input())
numbers = []
reverse_numbers = []
for _ in range(N):
    numbers.append(input().replace(' ', ''))
K = int(input())

def change_36_to_demical(x):
    if 48 <= ord(x) <= 57:
        return int(x)
    else:
        return ord(x) - 55

def change_demical_to_36(num):
    if 0 <= num <= 9:
        return str(num)
    else:
        return chr(num + 55)

# 중요도 계산(중요도, 위치)
importance = [[0, i] for i in range(36)]
for n in numbers:
    number = list(n)
    number.reverse()
    reverse_numbers.append(number)
    for i in range(len(number)):
        alpha = number[i]
        # 이미 Z는 변경할 필요 없음
        if alpha == 'Z':
            continue
        dnum = change_36_to_demical(alpha)
        # 자릿수와 숫자의 크기 모두로 중요도 계산(더 작은 숫자가 변경 중요도 높다)
        importance[dnum][0] += (35-dnum) * (36 ** i)

importance.sort(key=lambda x: -x[0])
importance = importance[:K]
change_num = []
for im in importance:
    change_num.append(im[1])

# 10진수로 계산한 숫자
demical_num = 0
for r_num in reverse_numbers:
    for i in range(len(r_num)):
        dnum = change_36_to_demical(r_num[i])
        # Z로 변환하는 숫자
        if dnum in change_num:
            dnum = 35
        demical_num += dnum * (36 ** i)

answer = ''
while demical_num:
    n = change_demical_to_36(demical_num % 36)
    demical_num //= 36
    answer = n + answer

# '002'와 같은 답일때 앞의 '00' 제거
answer = list(answer)
for i in range(len(answer)):
    if answer[i] != 0:
        answer = answer[i:]
        break
if answer:
    print(''.join(answer))
else:
    print('0')
