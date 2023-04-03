def solution(array):
    list_answer = "".join([str(i) for i in array])
    answer = list_answer.count("7")
    return answer