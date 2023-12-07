def solution(n, s):
    if n > s : return [-1]
    else :
        answer = []
        while n :
            t = s // n
            answer.append(t)
            s = s - t
            n -= 1

        return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12938