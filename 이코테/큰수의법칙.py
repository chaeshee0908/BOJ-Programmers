# 그리디 알고리즘

N,M,K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)     # 큰 수부터 정렬
first = data[0]     # 가장 큰 수
second = data[1]    # 두 번째로 큰 수

s_time = M // K
f_time = M - s_time

result = first * f_time + second * s_time

print(result)