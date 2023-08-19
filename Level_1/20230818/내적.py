def solution(a, b):
    answer = 0
    for i, j in zip(a, b) :
        answer += i * j
    return answer

def solution2(a, b) :
    return sum([i * j for i, j in zip(a, b)])