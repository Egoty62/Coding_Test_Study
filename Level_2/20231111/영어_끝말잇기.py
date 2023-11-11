def solution(n, words):
    last = words[0][0]
    worddict = {}
    for i in range(len(words)) :
        if (last == words[i][0]) and (words[i] not in worddict) :
            last = words[i][-1]
            worddict[words[i]] = 1
        else :
            a = (i + 1) % n
            b = (i + 1) // n
            return [n, b] if a == 0 else [a, b + 1]

    return [0, 0]

# https://school.programmers.co.kr/learn/courses/30/lessons/12981