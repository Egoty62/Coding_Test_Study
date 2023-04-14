# count() 사용
# 딕셔너리 사용

def solution(array):
    array_dict = {k : array.count(k) for k in array}
    number = 0
    for i in array :
        if number < array_dict[i] :
            number = array_dict[i]
            answer = i
    for k in array_dict.keys() :
        if k == answer : continue
        elif array_dict[k] == array_dict[answer] :
            return -1
    return answer