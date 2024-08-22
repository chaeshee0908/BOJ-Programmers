def solution(merchantNames):
    answer = []
    mer = sorted(merchantNames, reverse=True)
    symbol = ['&', '(', ')', '.', ',', '-']

    def check_name(symbol, name):
        s_list = list(name)
        s_str = ''
        for s in s_list:
            if s in symbol:
                continue
            if s == ' ':
                continue
            s_str += s
        return s_str

    while mer:
        origin_s = mer[0]
        mer = mer[1:]
        store = []
        store.append(origin_s)
        s_str = check_name(symbol, origin_s)
        s_max_len = len(s_str)
        for i, m in enumerate(mer):
            m_str = check_name(symbol, m)
            print(m_str, len(m_str))
            if m_str in s_str and len(m_str) == s_max_len:
                store.append(m)
            if m_str not in s_str:
                idx = i
                break
        mer = mer[i+1:]
        print(s_str, s_max_len, store)
        if len(store) == 1:
            answer.append(store[0])
        else:
            # 특수문자
            symbol_store = []
            for st in store:
                st_arr = list(st)
                for s in st_arr:
                    if s in symbol:
                        symbol_store.append(st)
            if len(symbol_store) == 0:
                for m in merchantNames:
                    if m in store:
                        answer.append(m)
                        break
            elif len(symbol_store) == 1:
                answer.append(symbol_store[0])
            else:
                for m in merchantNames:
                    if m in symbol_store:
                        answer.append(m)
                        break
                
 
    return answer
print(solution(["토스커피사일로 베이커리", "토스커피사일", "토스커피사일로 베이커", "토스커피사일로 베이", "토스커피사일로&베이커리"]))