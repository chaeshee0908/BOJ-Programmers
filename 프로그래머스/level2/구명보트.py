# 그리디 알고리즘

def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    cnt = 0
    while right - left >= 1:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        cnt += 1
    if left == right:
        cnt += 1
    return cnt

p1 = [40, 50, 150, 160]
p2 = [100, 500, 500, 900, 950]
print(solution(p1, 200))
print(solution(p2, 1000))        