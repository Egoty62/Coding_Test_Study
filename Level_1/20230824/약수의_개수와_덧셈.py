def solution(left, right):
    answer = 0
    for i in range(left, right + 1) :
        if (i ** 0.5).is_integer() :
            answer -= i
        else :
            answer += i
    return answer

# 리스트 컴프리헨션 사용

def solution2(left, right):
    return sum([i if not (i ** 0.5).is_integer() else -i for i in range(left, right + 1)])