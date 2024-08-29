# 구간합
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
n_sum = [0] * 100001
for i in range(N):
    n_sum[i+1] = n_sum[i] + numbers[i]

interval = []
for _ in range(M):
    interval.append(list(map(int, input().split())))
    
for i in range(M):
    a, b = interval[i][0], interval[i][1]
    print(n_sum[b] - n_sum[a-1])
