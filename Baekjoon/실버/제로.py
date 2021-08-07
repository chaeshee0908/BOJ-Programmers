# 10773번 (실버4)
# 구현, 자료 구조, 문자열, 스택

num = int(input())
n_list = []
for _ in range(num):
    n = int(input())
    # 0을 입력 받으면 입력받은 가장 최근 수 제거
    if n == 0:
        n_list.pop()
    else:
        n_list.append(n)

print(sum(n_list))