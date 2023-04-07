# 기약분수 만들기
    # a, b의 최대공약수 찾고, b / (최대공약수) 하기
        # 유클리드 호제법
# 기약분수에서 정수 b가 2, 5로만 이루어져 있는지 판단하기
    # 2로 계속 나누고 그 후 5로 계속 나눔
        # 나머지가 0이면 반복시행

def solution(a, b):
    a_temp = a
    b_temp = b
    gcd = 1
    
    while b_temp != 0 :
        n = a_temp % b_temp
        a_temp = b_temp
        b_temp = n
        if b_temp == 0 : gcd = a_temp
        
    b_temp = b / gcd
    for i in [2, 5] :
        while b_temp % i == 0 :
             b_temp = b_temp / i
    
    return 1 if b_temp == 1 else 2

# gcd 함수가 있었네...