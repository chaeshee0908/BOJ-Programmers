# 다이나믹 프로그래밍 알고리즘
# 링크 : https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

# 왼쪽 위, 위 비교해서 더 큰 값으로 초기화
def check_max(x, y):
    now = triangle[x][y]
    if y - 1 < 0:       # 왼쪽 위에 숫자가 없을 때
        return triangle[x-1][y] + now   
    elif y >= len(triangle[x]) - 1:     # 위에 숫자가 없을 때
        return triangle[x-1][y-1] + now     
    else:       # 두 위치 모두 숫자가 있을 때
        return max((triangle[x-1][y-1] + now), (triangle[x-1][y] + now))

def max_value():
    for i in range(1, N):
        for j in range(len(triangle[i])):
            triangle[i][j] = check_max(i, j)
    return max(triangle[N - 1])

N = int(input().rstrip())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().rstrip().split())))
print(max_value())
