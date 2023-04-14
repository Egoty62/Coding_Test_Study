# slicing 활용

# pop() 활용

def solution(num_list):
    return num_list[::-1]

def solution2(num_list) :
    answer = []
    while num_list :
        answer.append(num_list.pop())
    return answer