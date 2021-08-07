# 2839번 (브론즈1)
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘, 브루트포스 알고리즘

def bags(kg):
    b5 = kg//5
    if kg - (b5 * 5) == 0:
        return b5
    for i in range(b5, -1, -1):
        left = kg - (i * 5)
        if left % 3 == 0:
            return i + left // 3
    return -1

n = int(input())
print(bags(n))