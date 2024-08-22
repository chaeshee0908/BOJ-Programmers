# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
storage = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

d[0] = storage[0]
d[1] = max(d[0], storage[1])

for i in range(2, n + 1):
    d[i] = max(d[i - 2] + storage[i], d[i - 1])

print(d[n - 1])