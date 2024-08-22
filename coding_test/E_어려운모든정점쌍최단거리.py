import sys
input = sys.stdin.readline

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)


ver = []
N, M, K = map(int, input().rstrip().split())
for _ in range(M):
    ver.append(list(map(int, input().rstrip().split())))

if ver[0][0] in ver[-1]:
    print(0)
else:
    ret = f(N) / (f(2) * f(N-2)) - ((f(K) / (f(2) * f(K-2))) + (f(N-K) / (f(2) * f(N-K-2))))
    print(int(ret))