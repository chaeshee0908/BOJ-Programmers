# 18870번(실버3)
# 정렬, 값/좌표 압축

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
s_data = list(sorted(set(data)))    # 중복안된 정렬된 데이터
result = {}     # 딕셔너리 형태로

# 순위 넣어주기
for i in range(len(s_data)):
    result[s_data[i]] = i

for i in data:
    print(result[i], end=' ')