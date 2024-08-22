# 두번째 원소부터 앞의 적절한 위치에 넣기
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
for i in range(1, 10):
    for j in range(i, 0, -1):    # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]:   # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
    print(array)