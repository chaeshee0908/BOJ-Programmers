# 프로그래머스
# Lv3
# https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3

import heapq    

def solution(n, results):
    graph = [[] for _ in range(n+1)]
    # 순위를 확인할 수 있는지 확인하는 리스트
    checked = [False] * (n+1)
    for win, lose in results:
        # win이 lose를 이겨서 +1점
        graph[win].append((lose, 1))
        # lose가 win을 이겨서 -1점
        graph[lose].append((win, -1))
    
    # 승부 관계가 연결되어 있는 사람 수 찾기
    def find_person_num(q, person, score, visited):
        count = 0
        while q:
            score, person = heapq.heappop(q)
            for p, s in graph[person]:
                # 이전 상태와 점수가 같으면
                if s == score and not visited[p]:
                    heapq.heappush(q, (s, p))
                    visited[p] = True
                    count += 1
        return count

    # 순위를 확정할 수 있는 사람 수 찾기
    '''
    풀이: 이기고 질 때 점수를 1과 -1로 표현하여 이어지는 관계를 카운트해준다. 
    계속 이기거나 계속 지는 경우를 모두 합했을 때 n - 1(본인 제외 수)가 나온다면 해당 선수의 순위를 알 수 있다.
    '''
    for i in range(1, n+1):
        q = []
        cnt = 0
        visited = [False] * (n+1)
        for person, score in graph[i]:
            if visited[person]:
                continue
            cnt += 1
            if score == -1:
                heapq.heappush(q, (score, person))
                visited[person] = True
                cnt += find_person_num(q, person, score, visited)
            elif score == 1:
                heapq.heappush(q, (score, person))
                visited[person] = True
                cnt += find_person_num(q, person, score, visited)
        if cnt == n - 1:
            checked[i] = True
    
    # 순위 가능한 사람 수 반환
    return checked.count(True)

# test case       
n = 5
match = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, match))