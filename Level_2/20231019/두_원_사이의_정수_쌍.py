def solution(r1, r2):
    answer = 0
    
    for x in range(0, r2 + 1) :
        if r1 <= x : b = 0
        else :
            b = (r1 ** 2 - x ** 2) ** (1/2)
            if b != int(b) : b = int(b) + 1
        a = int((r2 ** 2 - x ** 2) ** (1/2))
        answer += a - b + 1
        
    answer -= r2 - r1 + 1
    
    return answer * 4

# https://school.programmers.co.kr/learn/courses/30/lessons/181187