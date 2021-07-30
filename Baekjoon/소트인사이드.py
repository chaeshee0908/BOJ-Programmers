# 문자열, 정렬

n = list(map(int,input()))
n.sort(reverse=True)
result = ''
for num in n:
    result += str(num)
print(result)
