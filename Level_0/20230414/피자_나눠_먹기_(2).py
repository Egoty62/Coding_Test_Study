# n과 6의 최소공배수 구하기
    # 최소공배수는 n * 6 / (n과 6의 최대공약수)
        # 구한 후 최소공배수 / 6을 반환
            # n / 최대공약수
# 최대공약수는 유클리드 호제법을 이용하여 구함
    # while문 사용

def solution(n):
    temp = 0
    a = n
    b = 6
    while b != 0 :
        temp = a % b
        a = b
        b = temp
    return n / a