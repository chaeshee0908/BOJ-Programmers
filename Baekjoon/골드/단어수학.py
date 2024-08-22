# 골드4 1339번
# https://www.acmicpc.net/problem/1339

N = int(input())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_num = [-1 for _ in range(26)]     # 알파벳 숫자 지정
now_num = 9
origin_words = []
words = []
for _ in range(N):
    word = input()
    origin_words.append(word)
    words.append([len(word), word])

words.sort(key=lambda x: x[0])

num_words = []  # 같은 길이의 단어끼리의 묶음
now_len, now_word = words.pop()
num_word = [now_len, now_word]
# 같은 길이 단어끼리 묶기
while words:
    next_len, next_word = words.pop()
    # 같은 길이의 단어일 때
    if now_len == next_len:
        num_word.append(next_word)
    # 다른 길이의 단어일 때
    else:
        num_words.append(num_word)
        now_len, now_word = next_len, next_word
        num_word = [now_len, now_word]

num_words.append(num_word)

# 알파벳 우선순위
alpha_order = [0 for _ in range(26)]

# 알파벳 우선순위 정하기
def order_alphabet(n, words):
    word_alphabet = []
    for word in words:
        plus_num = 10 ** (n-1)
        word = list(word)
        for w in word:
            word_alphabet.append(w)
            alpha_order[alphabet.index(w)] += plus_num
            plus_num //= 10
    
# 알파벳 숫자 정하기
def alphabet_to_number():
    global now_num
    # 단어에 포함된 모든 알파벳 우선순위 리스트
    alpha_order_list = []
    for i in range(26):
        if alpha_order[i] != 0:
            alpha_order_list.append([alpha_order[i], alphabet[i]])
    # 우선순위대로 정렬
    alpha_order_list.sort(key=lambda x: x[0], reverse=True)
    for aol in alpha_order_list:
        al_index = alphabet.index(aol[1])
        # 이미 알파벳에 숫자가 부여돼있을 때 
        if alpha_num[al_index] != -1:
            continue
        alpha_num[al_index] = now_num   # 숫자 지정
        now_num -= 1    # 숫자 1 줄이기

# 길이가 긴 단어부터 작은 순 대로 비교
for i in range(len(num_words)-1):
    n, w_list = num_words[i][0], num_words[i][1:]
    check_len = n - num_words[i+1][0]   # 확인해야할 자리 수(앞에서부터)
    check_word_list = []
    for w in w_list:
        check_word_list.append(w[:check_len])
        num_words[i+1].append(w[check_len:])
    order_alphabet(n, check_word_list)

# 가장 짧은 단어들 비교
order_alphabet(num_words[-1][0], num_words[-1][1:])

# 알파벳 숫자 지정
alphabet_to_number()

# 단어 숫자 더하기
def sum_alpha_num():
    result = 0
    for word in origin_words:
        num = ''
        for w in word:
            num += str(alpha_num[alphabet.index(w)])
        result += int(num)
    return result

print(sum_alpha_num())
