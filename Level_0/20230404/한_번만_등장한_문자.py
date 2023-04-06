def solution(s):
    temp = []
    answer = []
    for i in s :
        if i in temp :
            if i in answer :
                answer.remove(i)
        else :
            temp.append(i)
            answer.append(i)
    answer.sort()
    
    return ''.join(answer)