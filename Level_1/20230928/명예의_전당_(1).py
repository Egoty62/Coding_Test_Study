def solution(k, score):
    answer = []
    temp = []
    for i in score :
        temp.append(i)
        if len(temp) > k :
            temp.remove(min(temp))
        answer.append(min(temp))
    return answer