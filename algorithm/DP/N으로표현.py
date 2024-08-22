# 프로그래머스 
# Lv3
# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3

N = 5
number = 12

def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        # i : N의 개수
        all_case = set()
        check_number = int(str(N)*i)
        print()
        print('-----------------------')
        print(check_number)
        # {N}, {NN}, {NNN} ...
        all_case.add(check_number)
        print(all_case)

        print('테이블 :', dp)
        for j in range(0, i-1):
            # j개를 사용하여 만든 값들
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
            print(all_case)
        if number in all_case:
            answer = i
            break

        dp.append(all_case)

    return answer


print(solution(N, number))
