# 7 * result가 n이상인 가장작은 result를 구함
    # result는 n / 7 이상의 정수

def solution(n):
    return n // 7 if n % 7 == 0 else n // 7 + 1