# 정렬 알고리즘
# 링크 : https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

N = int(input().rstrip())
students = []
for _ in range(N):
    students.append(list(input().rstrip().split()))
S = sorted(students, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in S:
    print(student[0])