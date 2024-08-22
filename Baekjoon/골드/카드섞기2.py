# 골드5 21315
# https://www.acmicpc.net/problem/21315

from itertools import product

def shuffle(k):
    global cards
    # 1단계 섞기
    left = cards[:N-2**k]
    main_cards = cards[N-2**k:]
    # 나머지 섞기
    for i in range(2, k + 2):
        l = len(main_cards)
        left = main_cards[:l-2**(k-i+1)] + left
        main_cards = main_cards[l-2**(k-i+1):]
    
    return main_cards + left
        
N = int(input())
end_cards = list(map(int, input().split()))
k_cases = [i for i in range(1, N+1)]

for first, second in product(k_cases, repeat=2):
    cards = [i for i in range(1, N+1)]
    cards = shuffle(first)
    cards = shuffle(second)
    if cards == end_cards:
        print(first, second)
        break