def solution(survey, choices):
    answer = ''
    point = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    score = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) :
        if choices[i] < 4 :
            score[survey[i][0]] += point[choices[i]]
        else : score[survey[i][1]] += point[choices[i]]
        
    if score['R'] >= score['T'] : answer += 'R'
    else : answer += 'T'
    
    if score['C'] >= score['F'] : answer += 'C'
    else : answer += 'F'
    
    if score['J'] >= score['M'] : answer += 'J'
    else : answer += 'M'
    
    if score['A'] >= score['N'] : answer += 'A'
    else : answer += 'N'
    
    return answer