# 3036번 (실버3)
# 수학, 정수론, 유클리드 호제법(최대공약수)

def Euclidean(a, b):
    if a < b:
        a, b = b, a
    while b:
        mod = a % b
        a = b
        b = mod
    return a
        

n = int(input())
ring = list(map(int, input().split()))
f_ring = ring[0]
ring.pop(0)
for r in ring:
    if f_ring % r == 0:
        print("{}/1".format(f_ring//r))
    else:
        GCD = Euclidean(f_ring, r)
        print("{}/{}".format(f_ring//GCD, r//GCD))