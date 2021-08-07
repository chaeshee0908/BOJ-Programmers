# 13305번 (실버4)
# 그리디 알고리즘
# 58점 부분성공

num = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
money = 0
while len(city) > 1:
    min_price = min(city)
    idx = city.index(min_price)
    min_road = road[idx:len(city)-1]
    money += sum(min_road)*min_price
    city = city[:idx+1]
    city[idx] = 10001       # 리터당 가격은 최대 10,000이므로 이미 계산한 수는 그보다 큰 수로 바꿔줌
print(money)
