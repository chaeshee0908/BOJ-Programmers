# 7568번
# 브루트포스 알고리즘

person = int(input())
p_sizes = []
for _ in range(person):
    size = list(map(int, input().split()))
    p_sizes.append(size)
for A in p_sizes:
    rank = 1
    for B in p_sizes:
        if A[0] < B[0] and A[1] < B[1]:
            rank += 1
    print(rank, end=' ')