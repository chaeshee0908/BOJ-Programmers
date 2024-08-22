# 골드5 7490번
# https://www.acmicpc.net/problem/7490

def calculate(formula):
    ff = formula.replace(' ', '')
    return eval(ff)

def recur(formula, number):
    global N, result
    # 식 완료
    if number == N + 1:
        # 결과값이 0일 때
        if calculate(formula) == 0:
            result.append(formula)
        return
    recur(formula + ' ' + str(number), number + 1)
    recur(formula + '+' + str(number), number + 1)
    recur(formula + '-' + str(number), number + 1)

T = int(input())
for _ in range(T):
    N = int(input())
    result = []
    recur('1', 2)
    for i in range(len(result)):
        print(result[i])
    print()