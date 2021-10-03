# 동적계획법(DP)

n_line = [0, 1, 11, 111, 1111, 11111, 111111]
def recur(N, number, answer):
    num_list = list(map(lambda x: x * N, n_line))
    if number in num_list:
        answer += num_list.index(number)
        return answer
    # 나머지가 생겼을 때
    if number % N != 0:
        number *= N
        answer += 1
        if number in num_list:
            answer += num_list.index(number)
            return answer
        else:
            number -= N
            answer += 1
    else:
        # number의 자릿수
        n = len(list(str(number)))
        if number < num_list[n]:
            number -= num_list[n-1]
            answer += n-1
        else:
            number -= num_list[n]
            answer += n
    return recur(N, number, answer)

def solution(N, number):
    answer = 0
    return recur(N, number, answer)

print(solution(5, 12))
print(solution(2, 11))