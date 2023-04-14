# slicing 이용해서 뒤집기

# 문자를 하나하나씩 거꾸로 더하기

def solution(my_string):
    return my_string[-1 : -1001 : -1]   # my_string[::-1]도 됨

def solution2(my_string):
    answer = ''
    for i in my_string :
        answer = i + answer
    return answer