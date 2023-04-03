def solution(n):
    a = 1
    answer = 2
    while a ** 2 < n :
        a += 1
        if a ** 2 == n :
            answer = 1
            break
    return answer