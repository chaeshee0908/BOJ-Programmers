def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])    
    answer = max(triangle[-1])
    return answer

t = [
[7], 
[3, 8], 
[8, 1, 0], 
[2, 7, 4, 4], 
[4, 5, 2, 6, 5]
]

print(solution(t))