def solution(n):
    answer = 0
    a = str(n)
    b = list(a)
    for i in b :
        answer += int(i)
    return answer

def solution(n):
    return sum([int(i) for i in list(str(n))])