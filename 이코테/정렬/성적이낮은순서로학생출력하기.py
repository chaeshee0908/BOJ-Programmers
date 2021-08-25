n = int(input())
data = []
for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))    # 튜플 형태로 저장
data.sort(key=lambda student : student[1])
for student in data:
    print(student[0], end=' ')
