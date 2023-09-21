def solution(ingredient):
    answer = 0
    temp = ''
    
    for i in ingredient :
        temp = temp + str(i)
        if temp[-4:] == '1231' :
            temp = temp[:-4]
            answer += 1
            
    return answer