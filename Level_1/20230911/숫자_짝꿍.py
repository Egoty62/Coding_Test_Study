def solution(X, Y):
    answer = ''
    for i in range(10) :
        answer = (str(i) * min(X.count(str(i)), Y.count(str(i)))) + answer
        
    if len(answer) == 0 : return "-1"
    return '0' if answer[0] == '0' else answer

# functools 에서 Counter를 가져와서 해결할 수도 있음
    # functools가 아님 collection임