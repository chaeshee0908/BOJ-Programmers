picture = []
for _ in range(5):
    picture.append(list(input().rstrip()))

if picture[0][1] == picture[1][0] or picture[0][1] == picture[1][1]:
    picture[0][1], picture[0][0] = picture[0][0], picture[0][1]

flag = 1

for i in range(4):
    if flag == 0:
        if picture[i][1] == picture[i+1][0] or picture[i][1] == picture[i+1][1]:
            picture[i][1], picture[i][0] = picture[i][0], picture[i][1]
    if picture[i][0] == picture[i+1][0]:
        flag = 1
        picture[i+1][0], picture[i+1][1] = picture[i+1][1], picture[i+1][0]
    else:
        flag = 0

for i in range(5):
    print(''.join(picture[i]))
    