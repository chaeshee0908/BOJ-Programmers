def solution(box):
    n = len(box)
    # 박스 뒷쪽부터 숫자가 가능한 최댓값 보다 작은 경우
    for i in range(n-1, -1, -1):
        if box[i] * (i+1) < sum(box):
            # print(box[i]*(i+1), sum(box))
            print(box)
            box.pop()
        else:
            break

    print(box)
    n = len(box)
    print(sum(box), n)
    avg = sum(box) // n
    leave = sum(box) % n
    if leave:
        max_num = avg + 1
    else:
        max_num = avg
    print(max_num)
    
    # 박스의 가장 첫 번째 숫자가 가장 큰 수일 때
    if box[0] == max(box):
        print('first big')
        return box[0]

    for i in range(n-1, 0, -1):
        if box[i] > max_num:
            # # 앞에 더 큰 숫자들이 나와서 이동시키면 안될 때
            # if box[i-1] > max_num:
            #     a = (box[i-1] + box[i]) // 2
            #     box[i-1] += box[i] - a
            #     box[i] -= box[i] - a
            #     continue
            box[i-1] += (box[i] - max_num)
            box[i] -= box[i] - max_num
            print(box)
    return max(box)

box = [3, 5, 15, 19]
print(solution(box))