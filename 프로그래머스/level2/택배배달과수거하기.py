# 2023 KAKAO BLIND RECRUITMENT

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 배열이 모두 0인 경우
    zero_list = [0] * n
    if deliveries == pickups == zero_list:
        return answer
    
    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups))
        d_limit, p_limit = cap, cap
        while deliveries:
            # 배달 가능, 배달 불필요 집
            if deliveries[-1] <= d_limit:
                d_limit -= deliveries.pop()
            # 부분 배달
            else:
                deliveries[-1] -= d_limit
                break
        while pickups:
            # 픽업 가능, 픽업 불필요 집
            if pickups[-1] <= p_limit:
                p_limit -= pickups.pop()
            # 부분 픽업
            else:
                pickups[-1] -= p_limit
                break
            
    return answer * 2

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(2, 2, [0, 0], [0, 0]))