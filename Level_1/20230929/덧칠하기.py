def solution(n, m, section):
    answer = 0
    count = 0
    for i in section :
        if count == 0 :
            first = i
            count = 1
            answer += 1
        elif i >= first + m :
            first = i
            count = 1
            answer += 1
                
    return answer