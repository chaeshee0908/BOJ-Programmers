# 프로그래머스
# Lv3
# https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3

import copy

def solution(tickets):
    tickets_dict = dict()
    # 티켓 알파벳 순 정렬
    tickets.sort()
    # 티켓 개수
    n = len(tickets)
    for ticket in tickets:
        f, t = ticket
        if f in tickets_dict:
            tickets_dict[f].append([t, 0])
        else:
            tickets_dict[f] = [[t, 0]]
    
    # 모든 도시를 방문할 수 있는 경로 찾기
    def dfs(start):
        # 경로에 모든 비행기 표를 사용했다면
        # 풀이 : 모든 비행기 표를 사용했다면 사용한 비행기 표의 개수와 check의 수가 같아야 한다.
        for city_info in td[start]:
            city = city_info[0]
            visited = city_info[1]
            # 해당 도시에서 출발하는 티켓이 없는 경우 무시
            if city not in td:
                route.append(city)
                continue
            # 아직 방문하지 않았다면
            if visited == 0:
                route.append(city)
                # 방문 처리
                city_info[1] = 1
                dfs(city)
        return route

    # routes = []                    
    
    print(tickets_dict)
    td = copy.deepcopy(tickets_dict)
    route = ["ICN"]
    # 모든 도시를 포함하는 경로라면
    route_list = dfs("ICN")
    # if route_list:
    #     print('해당 경로는 가능한 경로입니다.')
    #     routes.append(route_list)
    
    return route_list

    # # 모두 만족하는 경로가 하나뿐이면
    # if len(routes) == 1:
    #     return routes[0]
    # # 가능한 경로가 없다면
    # elif len(routes) == 0:
    #     return -1
    # # 여러 개라면
    # else:
    #     result = routes[0]
    #     for r in routes:
    #         if r < result:
    #             result = r
    #     return r


tickets = [["ICN", "B"], ["B", "C"], ["C", "ICN"], ["ICN", "D"], ["ICN", "E"], ["E", "F"]]
print(solution(tickets))