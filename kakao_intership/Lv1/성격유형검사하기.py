# dictionary 사용

def solution(survey, choices):
    answer = ''
    eval = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(0, len(survey)):
        f, b = tuple(survey[i])
        if choices[i] < 4:
            eval[f] += 4 - choices[i]
        else:
            eval[b] += choices[i] - 4
    key = list(eval.keys())
    for i in range(0, 8, 2):
        f, b = eval[key[i]], eval[key[i+1]]
        if f == b:
            answer += min(key[i], key[i+1])
        elif f > b:
            answer += key[i]
        else:
            answer += key[i+1]
    return answer