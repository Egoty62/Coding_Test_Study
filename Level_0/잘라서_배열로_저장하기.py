def solution(my_str, n):
    answer = []
    m = 0
    l = n
    while len(answer) < len(my_str) / n :
        answer.append(my_str[m:l])
        m = l
        l += n        
    
    return answer