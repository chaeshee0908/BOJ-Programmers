flag = True
leaf = 0
def solution(numbers):
    global flag, leaf
    answer = []
    for x in numbers:
        x = bin(x)[2:]
        j = 2
        k = 0
        while j-1 < len(x):
            j = j * 2
            k = k + 1
        for _ in range(len(x), j-1):
            x = '0' + x
        flag = True
        leaf = 0
        if x[len(x)//2] == '0':
            answer.append(0)
            continue
        if len(x) == 1:
            answer.append(1)
            continue
        back(x, len(x)//2, 2**(k-1), True)
        answer.append(int(flag))
    return answer

def back(chr, num, dep, key):
    global flag, leaf
    if dep == 0:
        if chr[num] == '0':
            leaf += 1
        elif not key:
            flag = False
        return
    if chr[num] == '1' and not key:
        flag = False
        return
    if chr[num] == '0':
        key = False
    back(chr, num - dep, dep//2, key)
    back(chr, num + dep, dep//2, key)
