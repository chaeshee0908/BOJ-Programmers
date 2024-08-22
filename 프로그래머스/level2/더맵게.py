# 힙 알고리즘

import heapq

def solution(scoville, K):
    cnt = 0
    q = []
    while scoville:
        heapq.heappush(q, scoville.pop())
    flag = 1
    while flag:
        first = heapq.heappop(q)
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if not q and first < K:
            return -1
        # 음식이 한 개만 남았을 경우
        if not q:
            break
        second = heapq.heappop(q)
        if first >= K:
            flag = 0
            continue
        mix = first + second * 2
        cnt += 1
        heapq.heappush(q, mix)
    return cnt