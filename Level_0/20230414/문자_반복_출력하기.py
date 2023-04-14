# list로 나누고, list의 모든 원소(문자열)을 * 3 해준 뒤 join

def solution(my_string, n):
    answer_list = list(my_string)
    return ''.join([i * n for i in answer_list])
# 굳이 list로 만들지 않아도 됨

def solution2(my_string, n) :
    return ''.join([i * n for i in my_string])