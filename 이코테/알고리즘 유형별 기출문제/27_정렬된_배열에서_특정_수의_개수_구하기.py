# 이진 탐색 알고리즘

from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline

def count_x(array, x):
    l_idx = bisect_left(array, x)
    r_idx = bisect_right(array, x)
    if (r_idx - l_idx) == 0:
        return -1
    else:
        return r_idx - l_idx

N, x = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
print(count_x(array, x))