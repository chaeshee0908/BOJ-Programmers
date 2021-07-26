# 2798번
# 브루트포스 알고리즘

def blackjack(N, M, L):
    L.sort()
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                s = L[i] + L[j] + L[k]
                if s > max and s <= M:
                    max = s
    return max
    
N, M = map(int, input().split())
list1 = list(map(int, input().split()))
print(blackjack(N,M,list1))