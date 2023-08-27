def solution(n):
    n -= 1
    for i in range(2, n // 2 + 2) :
        if n % i == 0 : return i
    return n

# 리스트 컴프리헨션 사용

def solution2(n):
    n -= 1
    return [i for i in range(2, n + 1) if n % i == 0][0]

# 반복문의 범위가 위의 것이 절반이라 실행속도에서 우위를 가짐