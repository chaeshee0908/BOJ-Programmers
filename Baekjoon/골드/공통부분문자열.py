# 골드5 5582번
# https://www.acmicpc.net/problem/5582

str1 = input()
str2 = input()
# str1이 더 짧도록 수정
if len(str1) > len(str2):
    str1, str2 = str2, str1
length = len(str1)

dp = [0] * (length)
for idx in range(length):
    # 현재까지 찾은 최대 문자열 길이부터 탐색 
    start = max(dp)
    for l in range(start, length + 1):
        # str1의 범위를 넘어가면 break
        if idx + l > length:
            break
        t = str1[idx:idx+l]
        # 부분 문자열이 다른 문자열에 포함되어 있을 때 
        if t in str2:
            dp[idx] = max(dp[idx], l)
        else:
            break
print(max(dp))