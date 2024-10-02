# 투 포인터

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
answer = 2000000000
start, end = 0, 0

# end가 N이 되면 종료
while end < N:
    n1, n2 = numbers[start], numbers[end]
    # 두 숫자의 차이가 M일 때 -> 더 이상 작을 수 없음 return
    if abs(n1- n2) == M:
        answer = M
        break
    # 두 숫자의 차이가 M보다 작을 때 
    if abs(n1- n2) < M:
        end += 1
        continue
    # 두 숫자의 차이가 M보다 클 때
    answer = min(answer, abs(n1- n2))
    start += 1

print(answer)