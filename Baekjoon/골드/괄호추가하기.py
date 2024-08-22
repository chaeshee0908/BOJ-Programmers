# 16637번 골드3
# https://www.acmicpc.net/problem/16637

from itertools import combinations

N = int(input())
formula = list(input())
nums = []
oper_idx = []

for i in range(0, len(formula)):
    if i % 2 == 0:
        nums.append(int(formula[i]))
    else:
        oper_idx.append(i)

result = nums[0]

def calculate(n1, oper, n2):
    if oper == "*":
        return n1*n2
    if oper == "+":
        return n1+n2
    if oper == "-":
        return n1-n2

# 괄호가 겹치는게 없는지 확인 -> 괄호의 유효성 확인
def validation(tup):
    for i in range(len(tup)-1):
        if tup[i+1] - tup[i] <= 2:
            return False
    return True    

# 괄호가 없는 경우 계산
for i in range(1, len(formula), 2):
    result = calculate(result, formula[i], int(formula[i+1]))

# 새로운 괄호 식 값 계산
def new_formula_result(brackets):
    new_formula = []
    now_bracket = []
    # 새로운 식 생성
    for i in range(len(formula)):
        # 괄호에 포함되지 않을 때
        if i not in brackets:
            # 숫자일 때 
            if i % 2 == 0:
                new_formula.append(int(formula[i]))
            # 연산자일 때
            else:
                new_formula.append(formula[i])
        # 괄호에 포함될 때
        else:
            now_bracket.append(formula[i])
            # 괄호가 완성됐을 때
            if len(now_bracket) == 3:
                n1, oper, n2 = now_bracket
                new_formula.append(calculate(int(n1), oper, int(n2)))
                now_bracket = []
    # 새롭게 만들어진 식 계산
    new_answer = new_formula[0]
    for i in range(1, len(new_formula), 2):
        new_answer = calculate(new_answer, new_formula[i], new_formula[i+1])
    
    return new_answer

# 괄호가 있는 경우 계산
for i in range(1, len(formula)//2):
    for tup in combinations(oper_idx, i):
        # 괄호 배열이 유효하지 않은 경우
        if not validation(tup):
            continue
        # 괄호 배열이 유효한 경우
        brackets = []    # 괄호 내용 인덱스
        for t in tup:
            brackets += [t-1, t, t+1]  # 숫자, 연산자, 숫자 인덱스
        # 더 큰 값으로 초기화
        result = max(result, new_formula_result(brackets))

print(result)