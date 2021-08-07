# 2869번 (브론즈1)
# 수학

A, B, V = map(int,input().split())
day = ((V-A) / (A-B)) + 1
if day.is_integer() == False:
    day = day // 1 + 1
print(int(day))