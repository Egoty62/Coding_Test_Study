def solution(n, t, m, p):
    string = ''
    a = 0

    def convert(num_, int_) :
        temp = '0123456789ABCDEF'
        q = num_ // int_
        r = num_ % int_
        if q == 0 :
            return temp[r]
        else :
            return convert(q, int_) + temp[r]
    
    while len(string) < t * m :
        string = string + convert(a, n)
        a += 1

    answer = string[p-1::m]

    return answer[:t]

# https://school.programmers.co.kr/learn/courses/30/lessons/17687