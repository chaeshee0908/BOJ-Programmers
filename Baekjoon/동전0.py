# 11047번
# 그리디 알고리즘

count = 0
N, K = map(int, input().split())
coin_types = []
for _ in range(N):
    coin = int(input())
    coin_types.append(coin)
coin_types.reverse()

for coin in coin_types:
    count += K // coin
    K %= coin

print(count)