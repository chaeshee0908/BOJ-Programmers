# 구현 알고리즘
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/60057
# 합계 82.0/100.0 (11, 19, 22, 26, 27, 28)
# 주의할 예외 케이스 : 'acdhdh'인 경우 return이 6이 아니라 'ac2dh'로 5가 리턴되어야한다 

import sys
input = sys.stdin.readline

def compression(unit, s):
    unit_array = []

    for i in range(0, len(s), unit):
        if i + unit <= len(s):
            unit_array.append(''.join(s[i:i+unit]))
        else:
            unit_array.append(''.join(s[i:len(s)]))

    print('unit_array :', unit_array)

    repeat = 1
    final_str = ''

    for i in range(len(unit_array)-1):
        if unit_array[i] == unit_array[i+1]:
            repeat += 1
        else:
            if repeat != 1:
                final_str += (str(repeat) + unit_array[i])
                repeat = 1
            else:
                final_str += ''.join(unit_array[i])
        print('repeat :', repeat)
        print('final_str :',final_str)

    if repeat != 1:
        final_str += (str(repeat) + unit_array[-1])
        repeat = 1
    else:
        final_str += ''.join(unit_array[-1])
    print('repeat :', repeat)
    print('final_str :',final_str)

    f = list(final_str)

    return len(f)

def solution(s):
    unit = 500
    s = list(s)
    answer = len(s)

    for i in range(1, 501):
        start = 0
        end = i
        while end < len(s):
            front = ''.join(s[start:end])
            next = ''.join(s[end:end+i])
            start = end
            end = start + i
            if front == next:
                print('front : {}, next : {}'.format(front, next))                
                unit = i
                print('unit :', unit)
                result = compression(unit, s)
                print('result :',result)
                if answer > result:
                    answer = result  
                print('--------------------------------')
                break
    return answer

tmp_str = input().rstrip()
print('answer :',solution(tmp_str))
