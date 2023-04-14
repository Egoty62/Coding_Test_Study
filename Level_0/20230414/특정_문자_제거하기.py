# remove(letter) 사용

def solution(my_string, letter):
    answer_list = list(my_string)
    while letter in answer_list :
        answer_list.remove(letter)
    return ''.join(answer_list)

def solution2(my_string, letter) :
    return my_string.replace(letter, '')
