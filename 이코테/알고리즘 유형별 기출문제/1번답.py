n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
for i in data:
    print('adv :', i)
    count += 1
    print('count :',count)
    if count >= i:
        print('===> count >= adv')
        result += 1
        count = 0
    print()
print(result)