# 골드5 2116번
# https://www.acmicpc.net/problem/2116

'''
첫 시도는 첫 번째 놓는 주사위를 최선의 값으로 놓는 방법을 찾으려 접근하였으나, 모든 경우를 탐색하는 것이 최선의 방법을 찾는 방법으로 생각되어 변경
첫 주사위의 윗면을 6번 변경하여 6번 중 사각기둥의 옆면의 합이 가장 놓은 것을 고르면 된다.
이때 각 마주보는 면의 인덱스를 across라는 dictionary로 둔다.
'''

N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

across = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
# 각 경우마다 값 넣기
result_list = []

# 6면 중 위아래 제외 가장 큰 수
def find_max_num(up, down):
    dice_num = [i for i in range(1, 7)]
    dice_num.remove(up)
    dice_num.remove(down)
    return max(dice_num)

# 경우에 따른 한 면 최댓값 찾기
def calculate_max_sum(up, down, result):
    for i in range(1, len(dices)):
        down_idx = dices[i].index(up)
        down = up
        up = dices[i][across[down_idx]]
        result += find_max_num(up, down)
    return result
    
for a in across.keys():
    up, down = dices[0][a], dices[0][across[a]]
    result = find_max_num(up, down)
    result = calculate_max_sum(up, down, result)
    result_list.append(result)

print(max(result_list))
    
    