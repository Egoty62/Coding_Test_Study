# 2부터 n까지 소수를 구함
    # 소수 : 약수가 1과 자신밖에 없는 수
        # i 가 2 ~ (i // 2 + 1)의 범위에서 나머지가 0인 것이 없을 때 i는 소수
    # n을 나온 소수로 나눌 때 나머지가 0인 것들만 분리해서 반환

def solution(n):
    prime_list = []
    for i in range(2, n + 1) :
        prime = 1
        for j in range(1, i // 2 + 1) :
            if j == 1 : continue
            elif i % j == 0 :
                prime = 0
                break
        if prime == 1 :
            prime_list.append(i)
            
    return [i for i in prime_list if n % i == 0]