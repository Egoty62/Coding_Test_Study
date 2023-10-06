def solution(targets):
    answer = 0
    s, e = 0, 0
    targets.sort()
    
    for i, j in targets :
        if s <= i and i < e :
            s = i
            if j < e : e = j
        else :
            s = i
            e = j
            answer += 1
    return answer