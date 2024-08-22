# 골드5 2469번
# https://www.acmicpc.net/problem/2469

k = int(input())
n = int(input())
alpha = [chr(65 + i) for i in range(k)]
start_order = list(' '.join(alpha))
final_order = list(' '.join(list(input())))
h_len = len(start_order)
ladder = []
ladder.append(start_order)
for i in range(n):
    line = list(input())
    line = list(' ' + ' '.join(line) + ' ')
    if '?' in line:
        hidden = i + 1  # 물음표 가로줄 위치
    ladder.append(line)
ladder.append(final_order)

final_idx = []
for a in final_order:
    final_idx.append(start_order.index(a))

# 같은 알파벳 물음표에서 만나서 길찾기
def connect_road(idx):
    sx, sy = 0, idx
    ex, ey = n+1, final_idx.index(idx)
    # 위에서 물음표까지 내려가기
    while sx != hidden:
        sx += 1
        # 물음표 라인 도착시 움직이지 않도록 함
        if sx == hidden:
            break
        # 왼쪽에 막대기 있을 시 왼쪽으로 이동
        if 0 < sy - 1 and ladder[sx][sy - 1] == '-':
            sy -= 2
        # 오른쪽에 막대기 있을 시 오른쪽으로 이동
        elif sy + 1 < h_len and ladder[sx][sy + 1] == '-':
            sy += 2
    # 밑에서 물음표까지 올라가기
    while ex != hidden:
        ex -= 1
        # 물음표 라인 도착시 움직이지 않도록 함
        if ex == hidden:
            break
        # 왼쪽에 막대기 있을 시 왼쪽으로 이동
        if 0 < ey - 1 and ladder[ex][ey - 1] == '-':
            ey -= 2
        # 오른쪽에 막대기 있을 시 오른쪽으로 이동
        elif ey + 1 < h_len and ladder[ex][ey + 1] == '-':
            ey += 2
    # 가로 길이 차이가 3이상 날 경우(실제로는 가로 한 칸 차이보다 클 경우)
    if abs(sy - ey) > 2:
        return False    # 사다리 불가능한 경우
    # 다리를 안놔도 만나는 경우
    if sy == ey:
        return True
    # 다리 놓기(중복으로 놓기 가능)
    ladder[hidden][max(sy, ey)-1] = '-'
    return True

fail = False

for i in range(h_len):
    if start_order[i] == ' ':
        continue
    # 불가능한 경우
    if not connect_road(i): 
        print('x' * (k-1))
        fail = True
        break

if not fail:
    print(''.join(ladder[hidden]).replace(' ', '').replace('?', '*'))
