# 리스트의 값을 계속 더하되, Z가 있으면 그 전 값을 뺌
    # for문 쓰면 될 듯

def solution(s):
    s_list = s.split()
    answer = 0
    for i in range(len(s_list)) :
        if s_list[i] == 'Z' :
            answer -= int(s_list[i - 1])
        else : answer += int(s_list[i])
    return answer