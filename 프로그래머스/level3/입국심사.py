# 이분탐색

def solution(n, times):
    times.sort()
    start = 0
    end = times[-1] * n     # 최대시간 : 최대 심사시간 * 사람수
    check = []      # 검사하고자 하는 사람 수가 일치하는 시간의 리스트
    while start <= end:
        people = 0
        flag = 0    # 실질적으로 가능한 시간인지 체크
        mid = (start + end) // 2
        # mid 시간동안 심사 가능한 사람 수
        for x in times:
            people += mid // x
        # 사람 수가 입국심사 대상 수와 일치하면 
        if people == n:
            # 이전에 나왔던 숫자면 반복을 막기 위해 반복문 끝냄
            if pre == mid:
                break
            # mid가 times에서 나올 수 있는 시간인지 확인
            for x in times:
                # 가능한 시간이면 check에 넣어줌
                if mid % x == 0:
                    check.append(mid)
                    flag = 1
                    break
            # 불가능한 시간일 때 => 시간 줄여줌 
            if flag == 0:
                end = mid - 1
        # 심사 가능한 사람 수가 주어진 대상보다 적을 때 : 시간 늘려줌
        elif people < n:
            start = mid + 1
        # 심사 가능한 사람 수가 주어진 대상보다 많을 때 : 시간 줄여줌
        else:
            end = mid - 1
        # 이전 시간 기록
        pre = mid
    print(check)
    return min(check)    

n = int(input())
times = list(map(int, input().split()))
print(solution(n, times))
