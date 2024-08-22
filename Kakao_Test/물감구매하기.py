def solution(cost, x):
    n = len(cost)
    # 뒷 쪽 물감 가격이 가진 돈 보다 많은 경우
    for i in range(n-1, -1, -1):
        if cost[i] > x:
            del cost[i]
        else:
            break
    
    n = len(cost)
    
    # 같은 물감의 개수로 맞췄을 때 가격별 가치 비교
    same_value = [cost[i] * 2 ** (n - i - 1) for i in range(n)]
    print(same_value)
    paint_value = []
    for i in range(n):
        paint_value.append([same_value[i], i, cost[i]])
    paint_value.sort(reverse=True)
    print(paint_value)
    # 물감 개수
    paint_num = 0       
    idx = 0 
    # 돈을 다 쓸 때까지
    while x >= 0:
        if not paint_value:
            break
        sv, idx, i_cost = paint_value.pop()

        print(idx, i_cost)
        if len(paint_value) >= 2:
            idx1, i_cost1 = paint_value[-1][1], paint_value[-1][2]
            idx2, i_cost2 = paint_value[-2][1], paint_value[-2][1]
            if x - i_cost < i_cost1 and x >= i_cost1 + i_cost2:
                # 효율 1등보다 효율 2+3이 더 물감 개수가 많다면
                if 2 ** idx1 + 2 ** idx2 > 2 ** idx:
                    paint_num += 2 ** idx1 + 2 ** idx2
                    continue
        x -= i_cost
        if x < 0:
            break
        
        print(x)
        print('p_num',2**idx)
        paint_num += 2 ** idx
        print('paint_num',paint_num)

    return paint_num % ((10 ** 9)+7)

cost = [3, 4, 1]
x = 8
print(solution(cost, x))