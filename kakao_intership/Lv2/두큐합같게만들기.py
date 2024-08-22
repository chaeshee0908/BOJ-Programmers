from collections import deque

def solution(queue1, queue2):
    answer = 0
    goal = (sum(queue1) + sum(queue2)) // 2 
    M = (len(queue1)+len(queue2)) * 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    # 하나의 수가 평균보다 큰 수여서 불가능한 경우
    if max(q1) > goal or max(q2) > goal:
            return -1
    # 두 큐의 합이 홀수여서 불가능한 경우
    if q1_sum + q2_sum % 2 == 1:
        return -1
    while True:
        # 큰 쪽의 숫자를 작은 쪽 큐로 넘겨줌
        if q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q2_sum += num
            q1_sum -= num
            answer += 1
        elif q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
            answer += 1
        else:
            return answer
        # 각 큐의 원소 합을 같게 만들 수 없는 경우 (모든 경우를 다 시도해본 경우)
        if answer > M:
            return -1