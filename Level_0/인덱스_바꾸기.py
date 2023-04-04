def solution(my_string, num1, num2):
    temp = ''
    answer = list(my_string)
    temp = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = temp
    return ''.join(answer)