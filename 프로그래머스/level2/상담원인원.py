# 2023 현대모비스 알고리즘 경진대회 

from itertools import product
from collections import deque

def check_consult_finish(consult_list, now_category, req_time):
    c_list = consult_list.copy()
    finish = 0
    while c_list:
        end_time, category = c_list.popleft()
        # 이전 상담유형의 모든 상담 마무리 -> 상담 내역 없애기 
        if category != now_category:
            return (0, deque([]))
        # 현재 시점에서 이미 끝난 상담 확인
        if end_time <= req_time:
            finish += 1
            continue
        break
    
    cnt = finish
    while cnt:
        cnt -= 1
        consult_list.popleft()

    return (finish, consult_list)

def solution(k, n, reqs):
    # 멘토 n명
    mentor = range(1, n+1)
    reqs.sort(key=lambda x: x[2])

    # k개의 유형으로 나누는 모든 경우의 수 구하기 (중복순열)
    consulting_permutations = [p for p in product(mentor, repeat=k) if sum(p) == n]
    
    min_value = int(1e9)
    # 멘토 상담 배치 모든 경우
    for c in consulting_permutations:
        waiting = 0
        mentors = list(c)
        consult_list = deque([])
        for req in reqs:
            req_time, consult_time, category = req
            # 가장 빨리 끝나는 순으로 대기
            consult_list = deque(sorted(consult_list, key=lambda x: x[0]))
            # 멘토 상담 끝났으면 돌려놓기
            cnt, c_list = check_consult_finish(consult_list, category, req_time)
            mentors[category-1] += cnt
            consult_list = c_list
            # 배정할 멘토가 있을 시(상담 바로 가능)
            if mentors[category-1] > 0:
                mentors[category-1] -= 1
                consult_list.append((req_time + consult_time, category)) # 상담 배정
            # 배정할 멘토가 없을 시(대기 필요)
            else:
                end_time, category = consult_list.popleft()
                waiting += end_time - req_time
                consult_list.append((end_time + consult_time, category)) # 상담 배정
            
        min_value = min(min_value, waiting)

    return min_value

print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))