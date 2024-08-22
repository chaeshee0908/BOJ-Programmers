# 이진탐색 알고리즘
# 고정점 : 수열이나 원소 중에서 '그 값이 인덱스와 동일한 원소'

from sys import stdin
input = stdin.readline

def fixed_point(array, mid):
    start = 0
    end = len(array) - 1
    while start <= mid <= end:
        if array[mid] < mid:
            start = mid + 1
        elif array[mid] > mid:
            end = mid - 1
        else:
            return mid
        mid = (start + end) // 2
    return -1

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
print(fixed_point(array, N // 2))