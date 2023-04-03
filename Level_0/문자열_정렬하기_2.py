def solution(my_string):
    a = my_string.lower()
    answer = "".join(sorted(a))
    return answer