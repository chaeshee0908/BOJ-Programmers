# 해시
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    c_key = 0
    attribute = []
    for i in range(col):
        a = list(relation[x][i] for x in range(row))
        if len(set(a)) != row:
            attribute.append(a)
        else:
            c_key += 1
    for i in range(col):
        a = list(relation)
    print(c_key)

relation = [["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]

solution(relation)