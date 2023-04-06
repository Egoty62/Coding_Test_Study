def solution(before, after):
    answer = 1
    for i in before :
        if before.count(i) == after.count(i) : continue
        else : answer = 0
    return answer