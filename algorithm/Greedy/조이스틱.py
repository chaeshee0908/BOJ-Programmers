# 프로그래머스
# Lv2
# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def find_max_A(name):
    A_num = 0
    final_idx = 0
    idx = 0
    cnt = 0
    flag = 0
    fbA = 0
    fbIdx = 0
    fb = False
    # 처음이랑 끝에 이어진 A의 개수
    if name[0] == 'A' and name[-1] == 'A':
        # 처음 부분 A의 개수
        for i in range(len(name)):
            if name[i] != 'A':
                fbIdx = i
                break
            fbA += 1
        # 끝 부분 A의 개수
        for i in range(len(name) - 1, -1, -1):
            if name[i] != 'A':
                break
            fbA += 1
    for i in range(len(name)):
        # 다른 문자 제외 첫 시작 A일 경우
        if name[i] == 'A':
            cnt += 1
            if flag == 0:
                idx = i
                flag = 1
                
        # A 이후에 다른 문자일 경우
        elif name[i] != 'A' and flag == 1:
            flag = 0
            if A_num < cnt:
                A_num = cnt
                final_idx = idx
            cnt = 0
    if fbA > A_num:
        A_num = fbA
        final_idx = fbIdx
        fb = True
    print('Anum',A_num, final_idx)
    
    return (final_idx, fb)
    

def solution(name):
    cnt = -1
    name = list(name)
    n = len(name)
    a_name = list('A' * n)
    # 시작 인덱스 받아오기
    idx, fb = find_max_A(name)
    if idx == 0 or fb == True:
        move = 1
    else:
        move = -1
        idx -= 1    # 시작할 인덱스
    while a_name != name:
        x = idx
        print()
        print('-------------')
        print("{}번째".format(x+1))
        print(''.join(a_name), ''.join(name))
        print("{} -> {}".format(a_name[x], name[x]))
        diff = ord(name[x]) - ord(a_name[x])
        if diff > 13:
            cnt += 26 - diff
            print('알파벳수 조작: ', 26-diff)
        elif diff <= 13:
            cnt += diff
            print('알파벳수 조작: ', diff)
        # 문자 변경해줌
        a_name[x] = name[x]
        # 커서를 왼쪽으로 이동했을 때 문자 밖으로 나갈 때
        if move == -1 and x + move < 0:
            idx = n - 1
        else:
            idx = x + move
        cnt += 1
        print('커서 조작: 1')
        print('총합 : ',cnt)
    return cnt

name = "ABAAB"
print(solution(name))
            
        
            
            

            
            

