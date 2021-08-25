# 시간복잡도(평균) O(NlogN) 최악의 경우(이미 데이터가 정렬되어 있는 경우) : O(N^2)

data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(data, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        print(data)
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and data[left] <= data[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
            data[right], data[pivot] = data[pivot], data[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            data[right], data[left] = data[left], data[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(data, start, right - 1)
    quickSort(data, right + 1, end)

quickSort(data, 0, len(data)-1)
print(data)



