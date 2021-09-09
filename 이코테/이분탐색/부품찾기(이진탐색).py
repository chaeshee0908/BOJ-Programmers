import sys
input = sys.stdin.readline

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif target < array[mid]:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
N = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().rstrip().split()))
array.sort()    # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
M = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
find = list(map(int, input().rstrip().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for x in find:
    if binary_search(array, x, 0, N-1) == None:
        print('no', end=" ")
    else:
        print('yes', end=' ')