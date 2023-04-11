# 다항식에서 변수는 'x'밖에 주어지지 않고 기호는 + 밖에 없음
# split()을 사용하여 리스트로 만듦
    # 모든 'x'를 찾고, 앞의 계수를 분리해서 합침
    # 모든 정수를 찾고, 합침

def solution(polynomial):
    coefficient = 0
    constant = 0
    for j in polynomial.split() :
        if j[-1] == 'x' :
            if len(j) == 1 :    # 'x'만 있을 경우
                coefficient += 1
            else :
                coefficient += int(j[:-1])
        elif j == '+' : continue
        else :
            constant += int(j)
    
    if coefficient == 1 :   # x 앞의 계수 생략
        coefficient = ''

    if coefficient == 0 and constant == 0 :
        return '0'
    elif constant == 0 :
        return str(coefficient) + 'x'
    elif coefficient == 0 :
        return str(constant)
    else : return (str(coefficient) + 'x + ' + str(constant))