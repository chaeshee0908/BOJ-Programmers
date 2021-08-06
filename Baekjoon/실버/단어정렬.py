# 정렬

n = int(input())
words = []
for _ in range(n):
    words.append(input())
w = list(set(words))
w.sort()        # 사전 순 먼저 정렬
w.sort(key=len) # 그 후 길이 정렬
for word in w:
    print(word)