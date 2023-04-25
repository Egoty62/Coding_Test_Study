# 임의의 리스트를 생성

def solution(s, n):
    str_a = 'abcdefghijklmnopqrstuvwxyz' * 2
    str_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    answer = []
    for i in range(len(s)) :
        if s[i] in str_a :
            answer.append(str_a[list(str_a).index(s[i]) + n])
        elif s[i] in str_A :
            answer.append(str_A[list(str_A).index(s[i]) + n])
        else : answer.append(' ')
    return ''.join(answer)