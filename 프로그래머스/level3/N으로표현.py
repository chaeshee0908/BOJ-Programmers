# 동적계획법(DP)

def solution(N, number):
    # 이어 붙인 숫자 초기화 
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    # N 사용 횟수
    for cnt in range(8):
        for i in range(cnt):
            # N의 총 카운트 개수 중 i개
            for num1 in dp[i]:
                # N의 총 카운트 개수 중 i개를 제외한 나머지
                for num2 in dp[cnt-i-1]:
                    dp[cnt].add(num1 + num2)
                    dp[cnt].add(num1 - num2)
                    dp[cnt].add(num1 * num2)
                    if num2 != 0:
                        dp[cnt].add(num1 // num2)
        # number가 연산 결과에 있으면 리턴
        if number in dp[cnt]:
            return cnt + 1
        
    return -1

# print(solution(5, 12))
# print(solution(2, 11))
print(solution(8, 53))  # 5가 나와야함