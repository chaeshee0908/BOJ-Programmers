# 1032번 (브론즈1)
# 구현, 문자열

n = int(input())
files = []
ret = ''
for _ in range(n):
    files.append(input())
for i in range(len(files[0])):
    check = 0
    for j in range(len(files)-1):
        if files[j][i] != files[j+1][i]:
            check = 1
    if check == 1:
        ret += '?'
    else:
        ret += files[0][i]
print(ret)