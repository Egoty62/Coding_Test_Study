# 조건문을 만듦

def solution(dot):
    if dot[0] < 0 :
        if dot[1] < 0 :
            return 3
        else : return 2
    else :
        if dot[1] < 0 :
            return 4
        else : return 1

# 다른 사람의 풀이
def study(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
# True == 1, False == 0 인 것을 활용