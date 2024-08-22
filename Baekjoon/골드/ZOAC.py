# 골드5 16719번
# https://www.acmicpc.net/problem/16719

# 처음 입력받는 단어 리스트
start_word = list(input())
# 출력을 위한 단어 리스트(빈칸에서 채워나가기)
final_word = [' '] * len(start_word)
# 처음 입력받은 [단어, 위치] 리스트
word = [[start_word[i], i] for i in range(len(start_word))]

# 재귀를 사용한 단어 출력
def print_word(word):
    # 빈배열일 때 종료
    if not word:
        return
    # 단어 배열 알파벳 순으로 정렬
    sorted_word = sorted(word, key=lambda x:x[0])
    # 알파벳 중 가장 사전순으로 빠른 알파벳 처음 위치
    now_idx = sorted_word[0][1]
    # 출력을 위한 알파벳 채워넣기 
    final_word[now_idx] = start_word[now_idx]   # ' ' -> 알파벳
    # 사용한 알파벳 단어 리스트에서 삭제
    start_word[now_idx] = ''
    # 채워넣은 알파벳 합쳐서 출력 (빈칸은 없애고 출력)
    print(''.join(final_word).replace(' ', ''))
    # 사용한 알파벳 부분 배열 word에서의 인덱스 찾기 
    for i in range(len(word)):
        if word[i][1] == now_idx:
            word_idx = i
    # 해당 인덱스를 기준으로 좌우로 나누기
    print_word(word[word_idx+1:])   # 오른쪽 먼저 탐색
    print_word(word[:word_idx])     # 왼쪽 나중에 탐색

print_word(word)