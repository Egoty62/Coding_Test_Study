# range(), 리스트 컴프리헨션 사용

def solution(x, n):
    if x > 0 :
        answer = [i for i in range(x, x * n + 1, x)]
    elif x < 0 :
        answer = [i for i in range(x, x * n - 1, x)]
    else : answer = [0 for i in range(n)]
    return answer

def solution2(x, n):
    answer = [(i + 1) * x for i in range(n)]