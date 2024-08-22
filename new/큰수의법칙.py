N, M, K = map(int, input().split())
number = list(map(int, input().split()))

number.sort(reverse=True)
first = number[0]
second = number[1]

# M <= K
if M <= K:
    result = first * M
else:
    first_count = M // (K+1) * K + M % (K+1)
    result = first * (M//K) * K + second * (M-first_count)

print(result)

