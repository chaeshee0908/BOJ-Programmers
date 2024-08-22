from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split())) # (2^N-1)개
A_list = []

# 결제 금액 중 n개를 뽑아 상품 가격으로 설정
for c in combinations(S, n):
    A = list(c)
    # n개의 합이 S의 마지막 값(상품 금액 전부의 합)보다 커질 경우 확인 안해도 됨
    if sum(A) > S[-1]:
        break
    # n개의 합이 S의 마지막 값과 같을 경우 -> 가능한 경우(A_list)
    if sum(A) == S[-1]:
        A_list.append(sorted(A))

# 상품 금액 가능한 경우 탐색
for A in A_list:
    S_list = [] # 상품의 모든 가격 경우의 수
    # 각 상품의 개수별 가능 금액 모두 계산
    for i in range(1, n+1):
        for c in combinations(A, i):
            S_list.append(sum(c))
    # 정렬된 기준으로 입력된 결제 금액과 동일할 때 -> 상품 금액 리스트
    if sorted(S_list) == S:
        print(''.join([str(A[i]) for i in range(len(A))]))
        break