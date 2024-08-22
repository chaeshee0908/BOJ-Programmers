N = int(input())
result = -1

# 3의 배수 개수
for i in range(N//3+1):
    # 3의 배수를 제외했을 때 5의 배수가 되는 경우(나누어 떨어짐)
    if (N - (i*3)) % 5 == 0:
        result = i + (N - (i*3))//5
        break

print(result)