# 프로그래머스
# Lv1
# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost)
    reserve_set = set(reserve)
    lost = list(lost_set - reserve_set)
    reserve = list(reserve_set - lost_set)
    lost_num = len(lost)
    answer += n - lost_num
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            answer += 1
        elif r+1 in lost:
            lost.remove(r+1)
            answer += 1
    return answer

n = 4
lost = [2, 3]
reserve = [3, 4]
print(solution(n, lost, reserve))