# 홀수 번째 위치에는 '수', 짝수 번째 위치에는 '박' 입력

def solution(n):
    answer = '수박'
    return answer * (n // 2) if n % 2 == 0 else answer * (n // 2) + '수'