# 그리디 알고리즘

def make_A(alphabet):
    diff = ord(alphabet) - ord('A')
    if diff > 13:
         return (26 - diff)
    else:
        return diff

def solution(name):
    place_not_A = []
    move = 0

    # 문자중 'A' 아닌 곳 위치 파악
    for i in range(1,len(name)):
        if name[i] != 'A':
            place_not_A.append(i)
    
    # 첫 알파벳 'A'로 바꾸기
    if name[0] != 'A':
        move += make_A(name[0])

    # 조이스틱을 오른쪽 방향으로 가는 것이 더 가까울 때
    if place_not_A[0] <= len(name) - place_not_A[-1]:
        for i in range(1, len(name)):
            move += 1
            if name[i] != 'A':
                move += make_A(name[i])
    # 조이스틱을 왼쪽 방향으로 가는 것이 더 가까울 때
    else:
        for i in range(len(name)-1, 1, -1):
            move += 1
            if name[i] != 'A':
                move += make_A(name[i])
    return move

name1 = "JEROEN"
name2 = "JAN"
name3 = 'ABABAAAAAAABA'     # 10이 나와야함. 아마 한 방향만 고려해서 그런듯함
print(solution(name1))
print(solution(name2))
print(solution(name3))