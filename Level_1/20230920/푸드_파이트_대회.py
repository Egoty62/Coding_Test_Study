def solution(food):
    answer = ''
    temp = ''
    for i in range(1, len(food)) :
        answer += str(i) * (food[i] // 2)
    
    for i in answer :
        temp = i + temp
        
    return answer + '0' + temp