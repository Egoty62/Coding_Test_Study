def solution(p):
    if p == '' : return p
    else :
        a, b = 0, 0
        u = ''
        v = ''
        for i in p :
            if (a == 0 and b == 0) or a != b :
                u = u + i
                if i == '(' : a += 1
                else : b += 1
            else : v = v + i

        if u[-1] == ')' :
            return u + solution(v)
        else :
            n = len(u)
            empty = ''
            for i in range(n) :
                if i == 0 or i == n - 1 : continue
                else :
                    if u[i] == ')' :
                        empty = empty + '('
                    else : empty = empty + ')'
            return '(' + solution(v) + ')' + empty

# https://school.programmers.co.kr/learn/courses/30/lessons/60058