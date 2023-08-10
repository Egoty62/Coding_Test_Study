def solution(array, commands):
    answer = []
    for a in commands :
        i, j, k = a
        answer.append((sorted(array[i - 1 : j]))[k - 1])
    return answer