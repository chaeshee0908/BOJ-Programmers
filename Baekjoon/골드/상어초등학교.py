# 골드 5 21608번
# https://www.acmicpc.net/problem/21608

'''
1순위, 2순위에 따른 각 위치의 점수를 메긴다. 
1순위: 인접 위치에 좋아하는 사람이 있을 때마다 1000점을 부여한다.
2순위: 인접 위치에 사람이 없으면 100점을 부여한다.
각 자리 별로 1순위와 2순위를 종합한 점수를 메긴다. 이때 3순위인 위치는 가장 앞에 있는 자리를 선택하면 되기 때문에 굳이 점수를 메기지 않아도 된다.
점수와 자리 위치를 담은 배열([점수i, ri, ci])를 넣는다.
key=lambda를 통해 우선순위를 두어 배열을 정렬한다. (점수가 크고, r과 c가 작은 순서로)
정렬된 배열에서 가장 첫 번째에 위치한 배열이 가장 적합한 자리이다.
자리를 다 찾은 후 최종 점수를 메긴다.
'''

N = int(input())
like = []
classroom = [[0] * N for _ in range(N)]
student_like = [[] for _ in range(N**2 + 1)]
for _ in range(N**2):
    like.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 각 자리별 점수 메기기
def score(x, y, like):
    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            # 좋아하는 사람 주변일 때 -> 1000점(가장 큰 수를 부여한다)
            if classroom[nx][ny] in like:
                result += 1000
            # 인접한 칸이 비어있는 경우 -> 100점(두 번째로 큰 수를 부여)
            if classroom[nx][ny] == 0:
                result += 100
    return result              

for l in like:
    student, s_like = l[0], l[1:]
    student_like[student] = s_like
    s_score = []
    for i in range(N):
        for j in range(N):
            # 빈자리가 아닐 경우 패스
            if classroom[i][j] != 0:
                continue
            s = score(i, j, s_like)
            s_score.append([s, i, j])   # 1, 2번의 총평 및 위치
    best = sorted(s_score, key=lambda x: (-x[0], x[1], x[2]))   # 점수가 크고, 점수가 같으면 위치가 가장 앞인 자리
    best_score, best_x, best_y = best[0]
    classroom[best_x][best_y] = student

satisfaction = 0

# 인접 좋아하는 사람 수 확인
def check_love(x, y, student):
    num = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] in student_like[student]:
            num += 1
    return num
            
            
for i in range(N):
    for j in range(N):
        now_student = classroom[i][j]
        like_num = check_love(i, j, now_student)    
        # 인접한 사람 중 좋아하는 사람이 있을 때
        if like_num:        
            satisfaction += 10 ** (like_num - 1)

print(satisfaction)
    