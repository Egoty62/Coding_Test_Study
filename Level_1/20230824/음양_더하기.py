def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True :
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer

# 리스트 컴프리헨션 사용

def solution2(absolutes, signs):
    return sum([absolutes[i] if signs[i] == True else -absolutes[i] for i in range(len(absolutes))])