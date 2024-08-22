def find_nice_num(s):
    nice_num = []
    s_arr = list(s)
    if len(s_arr) < 3:
        return '-1'
    for i in range(len(s_arr)-2):
        a, b, c = s_arr[i], s_arr[i+1], s_arr[i+2]
        if a == b == c:
            nice_num.append(a+b+c)
    if nice_num:
        if max(nice_num) == '000':
            return '0'
        return max(nice_num)
    else:
        return '-1'


print(find_nice_num('000'))