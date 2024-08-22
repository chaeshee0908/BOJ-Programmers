# 골드5 2877번
# https://www.acmicpc.net/problem/2877

count = [2**i for i in range(31)]
K = int(input())

num = 0
for i in range(1, 31):
    num += count[i]
    if K <= num:
        num_len = i
        break

k_location = K - (num - count[num_len])
result = ''

div_num = 2
while num_len:
    n = k_location % div_num
    if n == 0 or n > (div_num // 2):
        result = '7' + result
    else:
        result = '4' + result
    num_len -= 1
    div_num *= 2

print(int(result))

