# 분모를 같게 하고, 분자를 그에 맞춰 바꿈
# 분자를 더한 값, 분모의 값을 이용하여 새로운 리스트 생성
# 분자와 분모의 최대공약수를 구해서 나눠준 리스트를 반환
    # 최대공약수는 유클리드 호제법 사용
    # math.gcd()도 있지만 유클리드 알고리즘에 익숙해지기 위해서 쓰지 않음

def solution(numer1, denom1, numer2, denom2):
    a = [numer1 * denom2, numer2 * denom1, denom1 * denom2]
    b = [a[0] + a[1], a[2]]
    while b[1] != 0 :
        temp = b[0] % b[1]
        b[0] = b[1]
        b[1] = temp
    return [(a[0] + a[1]) // b[0], a[2] // b[0]]