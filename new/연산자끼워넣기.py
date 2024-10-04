import sys

input = sys.stdin.readline
INF = int(1e9)

def dfs(n, temp):
    global mx, mn
    if n == N-1:
        mx = max(mx, temp)
        mn = min(mn, temp)
        return
    # 덧셈
    if operators[0] != 0:
        operators[0] -= 1
        dfs(n+1, temp + arr[n+1])
        operators[0] += 1
    # 뺄셈
    if operators[1] != 0:
        operators[1] -= 1
        dfs(n+1, temp - arr[n+1])
        operators[1] += 1
    # 곱셈
    if operators[2] != 0:
        operators[2] -= 1
        dfs(n+1, temp * arr[n+1])
        operators[2] += 1
    # 나눗셈
    if operators[3] != 0:
        operators[3] -= 1
        dfs(n+1, int(temp/arr[n+1]))
        operators[3] += 1

N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

mx = -INF
mn = INF
dfs(0, arr[0])

print(mx)
print(mn)