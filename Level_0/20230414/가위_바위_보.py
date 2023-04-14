# 가위는 2, 바위는 0, 보는 5로 표현
# 문자가 '2'면 '0', 문자가 '0'이면 '5', 문자가 '5'면 '2' 추가

def solution(rsp):
    answer = ''
    for i in rsp :
        if i == '0' :
            answer += '5'
        elif i == '2' :
            answer += '0'
        elif i == '5' :
            answer += '2'
    return answer