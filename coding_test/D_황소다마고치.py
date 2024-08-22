import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if 2 ** array[mid] <=  target < 2 ** array[mid+1]:
            return array[mid]
        elif target > 2 ** array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

array = [i for i in range(0, 43)]

T = int(input())
test_case = []
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    day = binary_search(array, n, 0, 43) + 1
    day += m
    print(day)
