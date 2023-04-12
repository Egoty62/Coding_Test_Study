# 문자열을 리스트로 만듦
    # try - except로 리스트 원소의 자료형을 int로 바꾼 뒤 sum()

def solution(my_string):
    list_my_string = list(my_string)
    answer = 0
    for i in list_my_string :
        try :
            answer += int(i)
        except ValueError : continue
    return answer

def solution2(my_string) :
    return sum([int(i) for i in my_string if i.isdigit() == True])