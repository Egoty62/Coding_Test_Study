def solution(n, money):
    money.sort()
    answerlist = [0 if i != 0 else 1 for i in range(n + 1)]
    
    for i in money :
        for j in range(i, n + 1) :
            answerlist[j] += answerlist[j - i]
        
    return answerlist[-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/12907