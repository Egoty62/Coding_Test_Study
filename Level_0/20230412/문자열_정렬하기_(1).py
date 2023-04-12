# isdigit()으로 숫자만 구분하고 sort로 정렬

def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])