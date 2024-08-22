# 2023 KAKAO BLIND RECRUITMENT

def solution(today, terms, privacies):
    answer = []
    dict_terms = {}
    today = list(map(int, today.split('.')))
    
    for t in terms:
        term, month = t.split(' ')
        dict_terms[term] = int(month)
        
    for i in range(len(privacies)):
        date, term = privacies[i].split(' ')
        p_date = list(map(int, date.split('.')))
        # 날짜 계산
        p_date[1] += dict_terms[term]
        if p_date[1] > 12:
            if p_date[1] % 12 == 0:
                p_date[0] += p_date[1] // 12 - 1
                p_date[1] = 12
            else:
                p_date[0] += p_date[1] // 12
                p_date[1] %= 12
        # 유효기간 지났을 시 파기
        if min(today, p_date) == p_date:
            answer.append(i+1)
        
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))