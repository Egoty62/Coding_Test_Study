def solution(array):
    result = 0
    for i in array :
        if result < i :
            result = i
    for j in range(len(array)) :
        if result == array[j] :
            index = j
    answer = [result, index]
    return answer