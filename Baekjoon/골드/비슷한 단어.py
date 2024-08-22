# 골드4 2179번
# https://www.acmicpc.net/problem/2179

from collections import Counter

N = int(input())
words = []
max_prefix_len = 0  # 접두사의 최대 길이
for _ in range(N):
    word = input()
    max_prefix_len = max(max_prefix_len, len(word))
    words.append(word)

# M의 길이의 접두사 만들고 확인 
def check_prefix(M):
    prefix = []
    for w in words:
        prefix.append(w[:M])
    dict_prefix = Counter(prefix)
    
    result = []
    for key in dict_prefix.keys():
        if dict_prefix[key] > 1:
            result.append(key)
    return result

prefix = []
# 가장 긴 접두사 찾기
while max_prefix_len:
    prefix = check_prefix(max_prefix_len)
    if prefix:
        break
    max_prefix_len -= 1

idx = 0
# 접두사를 포함하는 가장 첫 단어 찾기(접두사도 찾기)
for i in range(len(words)):
    if words[i][:max_prefix_len] in prefix:
        prefix = words[i][:max_prefix_len]
        idx = i + 1
        print(words[i])
        break

# 확정된 접두사에 해당하는 두 번째 단어 찾기
for i in range(idx, len(words)):
    if words[i][:max_prefix_len] == prefix:
        print(words[i])
        break
