def solution(a, b, n):
    empty = n
    answer = n
    while empty >= a :
        answer += (empty // a) * b
        empty = (empty // a) * b + empty % a
        
    
    return answer - n