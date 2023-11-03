from itertools import permutations as perm

def solution(k, dungeons):
    answer = 0
    dungeons = [i for i in dungeons if i[0] <= k]
    print(dungeons)
    n = k

    for i in range(len(dungeons) + 1) :
        bull = False
        for j in perm(dungeons, i) :
            if k < sum([i[1] for i in j]) : continue
            else :
                n = k
                for a, b in j :
                    if n < a :
                        bull = False
                        break
                    else :
                        n -= b
                        bull = True
                if n >= 0 and bull == True :
                    if answer < i :
                        answer = i
            print(j, bull)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/87946