# 해시 알고리즘

def solution(clothes):
    cnt = 1
    dic = dict()
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
    for key in dic:
        cnt *= (dic[key] + 1)   # 착용 안하는 경우 + 1
    return cnt - 1      # 모두 착용 안하는 경우 한 개 제외
        

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))