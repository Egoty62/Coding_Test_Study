def solution(s):
    answer = 0
    first = ''
    for i in range(len(s)) :
        if first == '' :
            first = s[i]
            a = 1
            b = 0
        else :
            if s[i] == first :
                a += 1
            else :
                b += 1
        
        if a == b :
            first = ''
            answer += 1
        else :
            if i == len(s) - 1 :
                answer += 1
                
    return answer