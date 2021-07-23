def solution(places):
    answer = [-1]*5
    for room in places:
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if i >= 1 and j >= 1:
                        if room[i-1][j] == 'P' or room[i][j-1] == 'P':
                            answer[places.index(room)] = 0
                        else:
                            if answer[places.index(room)] == -1:
                                answer[places.index(room)] = 1
                    if answer == 0:
                        break
                    if i >= 2 and j >= 2:
                        if room[i-1][j] == 'P' or room[i][j-1] == 'P':
                            answer[places.index(room)] = 0
                        elif room[i-2][j] == 'P':
                            if room[i-1][j] == 'X':
                                if answer[places.index(room)] == -1:
                                   answer[places.index(room)] = 1
                            else:
                                answer[places.index(room)] = 0
                                break
                        elif room[i-1][j-1] == 'P':
                            if room[i][j-1] == 'X' and room[i-1][j] == 'X':
                                if answer[places.index(room)] == -1:
                                   answer[places.index(room)] = 1
                            else:
                                answer[places.index(room)] = 0
                                break
                        elif room[i][j-2] == 'P':
                            if room[i][j-1] == 'X':
                                if answer[places.index(room)] == -1:
                                    answer[places.index(room)] = 1
                            else:
                                answer[places.index(room)] = 0
                                break
                    if answer == 0:
                        break
                    if i >= 0 and j >= 1 and i < 4:
                        if room[i+1][j-1] == 'P':
                            if room[i][j-1] == 'X' and room[i+1][j] == 'X':
                                if answer[places.index(room)] == -1:
                                    answer[places.index(room)] = 1
                            else:
                                answer[places.index(room)] = 0
                else:
                    if answer[places.index(room)] == -1:
                        answer[places.index(room)] = 1
    return answer

places = [["POOOP","OXXOX", "OPXPX", "OOXOX","POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
["OXPOO", "OPXOO", "OOOOO", "OOOOO", "OOOOO"],
["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]

print('answer :', solution(places))