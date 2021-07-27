# 구현

# 한수인지 확인하는 함수
def is_han(n):
    n_list = list(map(int, str(n)))
    diff = n_list[1] - n_list[0]
    for i in range(2,len(n_list)):
        if n_list[i] - n_list[i-1] != diff:
            return False
    return True

num = int(input())
count = 0
for i in range(1,num+1):
    if i < 100:
        count += 1
    else:
        if is_han(i):
            count += 1
print(count)