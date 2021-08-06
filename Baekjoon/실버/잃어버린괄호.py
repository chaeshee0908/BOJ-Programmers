# 1541번 (실버2)
# 문자열, 그리디 알고리즘, 파싱

# 식을 숫자 배열로 만들어줌
def make_num(st):
    num = []
    s = list(st)
    sign = ''
    value = ''
    for w in s:
        if w == '+' or w == '-':
            # 부호와 값 모두 있을 때
            if value and sign:
                num.append(int(sign+value))
                value = ''
            # 값만 있을 때(양수)
            elif value:
                num.append(int(value))
                value = ''
            sign = w
        else:
            value += w
    num.append(int(sign+value))
    return num

# -값 이후의 값은 모두 음수로 가정
def min_value(num_list):
    result = 0
    # 음수가 시작되는 인덱스
    idx = -1
    for n in num_list:
        if n < 0:
            idx = num_list.index(n)
            break
    if idx == -1:
        return sum(num_list)
    else:
        for i in range(idx):
            result += num_list[i]
        for i in range(idx, len(num_list)):
            result += -abs(num_list[i])
        return result

exp1 = input()
nums = make_num(exp1)
print(min_value(nums))
