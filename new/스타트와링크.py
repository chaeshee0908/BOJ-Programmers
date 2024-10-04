import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
visited = [False for _ in range(N)]
result = INF

# depth: 선택한 팀원 수, 선택한 팀원 번호
def backtracking(depth, idx):
    global result
    # 전체 인원의 반을 선택해서 뽑았을 때 
    if depth == N // 2:
        start_power, link_power = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_power += S[i][j]      # 선택한 인원 -> 스타트 팀
                elif not visited[i] and not visited[j]:
                    link_power += S[i][j]       # 선택 안한 인원 -> 링크 팀
        result = min(result, abs(start_power - link_power))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False

backtracking(0, 0)
print(result)
