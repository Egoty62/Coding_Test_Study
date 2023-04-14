# 짝수만 포함된 리스트를 만들고, sum()하기

def solution(n):
    return sum([i for i in range(1, n + 1) if i % 2 == 0])

def solution2(n) :
    return sum([i for i in range(2, n + 1, 2)])