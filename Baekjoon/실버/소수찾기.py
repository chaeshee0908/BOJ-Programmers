# 1978번 (실버4)
# 수학, 정수론, 소수 판정, 에라토스테네스의 체

def prime_number(num):
    if num == 1:
        return False
    elif num == 2 or num == 3 or num == 5:
        return True
    else:
        div = (num // 2)
        for i in range(2,div+1):
            if num % i == 0:
                return False
    return True

n = int(input())
datas = list(map(int,input().split()))
result = 0
for data in datas:
    if prime_number(data):
        result += 1
print(result)