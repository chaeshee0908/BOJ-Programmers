# 골드4 1062번
# https://www.acmicpc.net/problem/1062

from collections import Counter

# N, K = map(int, input().split())
words = ''
essential_alpha = ['a', 'c', 'i', 'n', 't']

# for _ in range(N):
#     word = input()
#     l = len(word)
#     word = word[4:l-4]
#     words += word

bit = 0
bit = bit | (1 << ord('i') - ord('a'))
print(bit)

# # 'anta'와 'tica'는 무조건 들어가는 단어이므로 a, c, i, n, t 5개는 무조건 가르쳐야함
# if K < 5:
#     print(0)
# else:
#     words = list(words)
#     words_set = list(words)
#     sorted_alpha = []
#     for w in words_set:
#         if w in essential_alpha:
#             continue
#         sorted_alpha.append((words.count(w), w))
    
