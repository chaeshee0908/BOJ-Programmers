# 7568번
# 브루트포스 알고리즘

person = int(input())
p_sizes = []

# 각각의 사이즈 입력 받기
for _ in range(person):
    size = list(map(int, input().split()))
    p_sizes.append(size)

for A in p_sizes:
    rank = 1
    for B in p_sizes:
        # 자신보다 몸무게와 키 모두 큰 사람 수 + 1이 본인의 등수
        if A[0] < B[0] and A[1] < B[1]:
            rank += 1
    print(rank, end=' ')