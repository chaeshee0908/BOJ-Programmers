# 가장 작은 숫자를 선택하여 앞과 바꾼다. 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
for i in range(9):
    min_value = array[i]
    min_index = i
    for j in range(i+1, 10):
        if min_value > array[j]:
            min_value = array[j]
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    print(array)

