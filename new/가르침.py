import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = []
for _ in range(N):
    words.append(input().rstrip())

# z-a 순으로 bit 생성 
def word_to_bit(word):
    bit = 0
    for c in word:
        bit = bit | (1 << ord(c) - ord('a'))
    return bit

base_bit = word_to_bit('acint')
bits = []
for word in words:
    bits.append(word_to_bit(word))

if K < 5:
    print(0)
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    answer = 0
    for comb in combinations(alphabet, K-5):
        know_bit = sum(comb) | base_bit
        cnt = 0
        for bit in bits:
            if bit & know_bit == bit:
                cnt += 1
        answer = max(answer, cnt)
    print(answer)