def solution(common):
    if common[1] - common[0] == common[2] - common[1] :
        n = common[1] - common[0]
        answer = common[-1] + n
    elif common[1] / common[0] == common[2] / common[1] :
        n = common[1] / common[0]
        answer = common[-1] * n
    return answer