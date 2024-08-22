N, K = map(int, input().split())
choco = list(map(int, input().split()))
eat = 0
day = 0

flag = 0
idx = K + 1
while True:
    while choco[idx-1] == choco[idx-K-1]:
        idx += 1
        if idx > len(choco):
            flag = 1
            break

    if flag == 1:
        break
    
    if choco[idx-1] != choco[idx-K-1]:
        eat += choco[idx-1] - choco[idx-K-1]
        choco[idx-1] = choco[idx-K-1]
        day += 1
    

    if idx != len(choco):
        idx += 1
    
    choco.sort()
    
print(eat, day)
        