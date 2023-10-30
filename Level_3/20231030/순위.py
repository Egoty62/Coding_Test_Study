def solution(n, results):
    answer = 0
    winlinked = {i : [] for i in range(1, n + 1)}
    loselinked = {i : [] for i in range(1, n + 1)}

    for i, j in results :
        if i not in loselinked[j] :
            loselinked[j].append(i)
            
        if j not in winlinked[i] :
            winlinked[i].append(j)

    for k in range(1, n + 1) :
        for l in winlinked[k] :
            for temp in winlinked[l] :
                if temp not in winlinked[k] :
                    winlinked[k].append(temp)
        for l in loselinked[k] :
            for temp in loselinked[l] :
                if temp not in loselinked[k] :
                    loselinked[k].append(temp)

    for i in range(1, n + 1) :
        count = 0
        count += len(winlinked[i])
        count += len(loselinked[i])

        if count + 1 == n :
            answer += 1

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/49191