def solution(elements):
    answer = []
    n = len(elements)
    elements = elements * 2

    for i in range(1, n + 1) :
        for j in range(n) :
            a = sum(elements[j : j + i])
            answer.append(a)
        
    return len(set(answer))

def solution2(elements):
    answer = set()
    n = len(elements)
    elements = elements * 2

    for i in range(1, n + 1) :
        for j in range(n) :
            a = sum(elements[j : j + i])
            answer.add(a)
        
    return len(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/131701
