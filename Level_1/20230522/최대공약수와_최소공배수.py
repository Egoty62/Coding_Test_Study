# 최대공약수와 최소공배수 구하기
# 유클리드 호제법 사용

def euclid(a, b) :
    while b != 0 :
        temp = a % b
        a = b
        b = temp
        if b == 0 :
            return a
        
# 최소공배수는 초기 (a * b) / gcd

def solution(n, m):
    a, b = n, m
    gcd = euclid(a, b)
    lcm = n * m / gcd
    
    return [gcd, lcm]