# 2021 KAKAO BLIND RECRUITMENT

from itertools import combinations

def solution(orders, course):
    course_list = []
    o_list = []
    answer = []
    for order in orders:
        o_list.append(list(order))
    for c in course:
        group = []
        for order in o_list:  
            for comb in combinations(order, c):
                comb = list(comb)
                comb.sort()
                group.append(tuple(comb))
        course_list.append(group)
    
    for c in course_list:
        set_course = set(c)
        dict_c = dict()
        for s in set_course:
            dict_c[s] = c.count(s)
        if not dict_c:
            continue
        all_values = dict_c.values()
        max_value = max(all_values)
        for key in dict_c:
            if dict_c[key] == max_value and max_value != 1:
                str = ''.join(key)
                answer.append(str)
    answer.sort()
    return answer
        
o1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
o2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
o3 = ["XYZ", "XWY", "WXA"]
c1 = [2,3,4]
c2 = [2,3,5]
c3 = [2,3,4]
print(solution(o1, c1))
print(solution(o2, c2))
print(solution(o3, c3))