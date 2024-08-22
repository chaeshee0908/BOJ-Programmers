# Lv2
w, h = map(int, input().split())

def solution(w, h):
    answer = 0
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w * h - w
    else:
        # 일차함수로 생각 y = ax + b
        a, b = -(h/w), h
        for i in range(1, w):
            num = int(a * i + b)
            answer += num
    return answer * 2

print(solution(w, h))