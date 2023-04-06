def solution(quiz):
    temp = []
    answer = []
    for i in quiz :
        temp.append("".join(list(i)).split())
        
    for j in temp :
        if '+' in j :
            if int(j[0]) + int(j[2]) == int(j[-1]) :
                answer.append('O')
            else : answer.append('X')
        elif '-' in j :
            if int(j[0]) - int(j[2]) == int(j[-1]) :
                answer.append('O')
            else : answer.append('X')
    return answer