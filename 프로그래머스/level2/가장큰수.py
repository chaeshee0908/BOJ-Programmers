# 정렬

def solution(numbers):
    check = 0
    # numbers가 0으로만 되어있을 경우
    for number in numbers:
        if number != 0:
            check = 1
    if check == 0:
        return '0'
    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda x : x*3, reverse=True)  # number은 1000이하의 숫자이기 때문에 최댓값 생각해서 3곱해줌
    return ''.join(numbers)

numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers1))
print(solution(numbers2))