a = []
while 1:
    s = input().strip()
    if s != "":
        s = list(s)
        flag = 0
        if s[0] == '-':
            flag = 1
            s = s[1:]

        if '.' in s:
            dot_index = s.index('.')
            if len(s) >= dot_index + 3:
                s = s[:dot_index + 3]
            else:
                while len(s) < dot_index + 3:
                    s.append('0')
        else:
            s.append('.')
            s.append('0')
            s.append('0')
            dot_index = s.index('.')
        j = dot_index - 3
        while j > 0:
            s.insert(j, ',')
            j -= 3

        s.insert(0, '$')
        if flag:
            s.insert(0, '(')
            s.append(')')
        print(''.join(s))
    else:
        break