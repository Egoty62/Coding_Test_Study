def solution(progresses, speeds):
    answer = []
    def div(a, b) :
        q, r = divmod(a, b)
        if r != 0 :
            q += 1
        return q
    
    day = [div(100 - i, j) for i, j in zip(progresses, speeds)]

    a = 0
    b = 0
    for i in day :
        if a == 0 :
            a = i
            b = 1
        elif i > a :
            a = i
            answer.append(b)
            b = 1
        else : b += 1
    answer.append(b)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42586