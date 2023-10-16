def solution(s):
    stacklist = []
    for i in s :
        if i == '(' :
            stacklist.append(0)
        else :
            try :
                stacklist.pop()
            except IndexError :
                return False

    return True if len(stacklist) == 0 else False

# https://school.programmers.co.kr/learn/courses/30/lessons/12909