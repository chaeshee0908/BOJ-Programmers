# 11047번
# 그리디 알고리즘

count = 0
N, K = map(int, input().split())
coin_types = []
for _ in range(N):
    coin = int(input())
    coin_types.append(coin)
coin_types.reverse()    # 큰 순서대로 정렬

for coin in coin_types:
    count += K // coin
    K %= coin

print(count)