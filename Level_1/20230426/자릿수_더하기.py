# 자연수 n을 str로 변환
    # list로 만들고 다시 int로 만들어서 더하기

def solution(n):
    return sum([int(i) for i in str(n)])