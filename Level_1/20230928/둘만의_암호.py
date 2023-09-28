def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz" * 3
    temp = [i for i in alpha if i not in skip]
    
    for i in s :
        answer += temp[temp.index(i) + index]
    return answer