# 복서 정렬하기
def order(weights, array):
    ret = []
    while array:
        ret.append(weights[array.index(max(array))])
        weights.pop(array.index(max(array)))
        array.pop(array.index(max(array)))
    return ret

def solution(weights, head2head):
    answer = []
    boxer = weights[:]
    win_rate = []
    win_heavy = []
    weights.sort(reverse=True)     # 3번 조건
    # 2번 조건
    for i in range(len(head2head)):
        wh = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    wh += 1
        win_heavy.append(wh)
    weights = order(weights, win_heavy)
    #  1번 조건
    for i in range(len(head2head)):
        wr = 0
        fight = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                fight += 1
            if head2head[i][j] == 'W':
                wr += 1
        if fight == 0:
            wr = 0
        else:
            wr = 100 * (wr / fight)
        win_rate.append(wr)
    weights = order(weights, win_rate)
    for i in range(len(boxer)):
        num = boxer.index(weights[i]) + 1
        if num in answer:
            rest_list = list(filter(lambda x: boxer[x] == weights[i], range(len(boxer))))
            while (rest_list[0] + 1) in answer:
                rest_list.pop(0)
            num = rest_list[0] + 1
        answer.append(num) 
    return answer

w1 = [50,82,75,120]
w2 = [145,92,86]
w3 = [60,70,60]
hh1 = ["NLWL","WNLL","LWNW","WWLN"]
hh2 = ["NLW","WNL","LWN"]
hh3 = ["NNN","NNN","NNN"]
print(solution(w1, hh1))
print(solution(w2, hh2))
print(solution(w3, hh3))
