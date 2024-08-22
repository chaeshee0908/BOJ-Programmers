# 구현 알고리즘

import sys
import re
input = sys.stdin.readline

tmp_str = list(input().rstrip())
n_sum = 0
onlyStr = []
for s in tmp_str:
    if ord(s) < 65:
        n_sum += int(s)
    else:
        onlyStr.append(s)
onlyStr.sort()
print(''.join(onlyStr) + str(n_sum))