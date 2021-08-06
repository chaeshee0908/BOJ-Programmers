# 11399번 (실버 3)
# 그리디 알고리즘
# 정렬

person = int(input())
times = list(map(int,input().split()))

times.sort()
result = 0
for _ in range(person):
    result += sum(times)
    times.pop() 
print(result)