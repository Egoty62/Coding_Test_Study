def solution(n, wires):
    answer = []
    wirelist = []
    wirelink = {i : {} for i in range(1, n + 1)}
    for i in wires :
        wirelink[i[0]][i[1]] = 0
        wirelink[i[1]][i[0]] = 0

    

    for i in range(1, n + 1) :
        start = {i : False for i in range(1, n + 1)}
        queue = []
        start[i] = True
        
        for j in wirelink[i] :
            start[j] = True
            queue.append(j)
            num = 1

            while queue :
                a = queue.pop(0)
                for k in wirelink[a].keys() :
                    if start[k] == False :
                        queue.append(k)
                        start[k] = True
                        num += 1
                    else : continue

            wirelink[i][j] = num

    for i in range(1, n + 1) :
        for j in wirelink[i] :
            wirelist.append(wirelink[i][j])

    for i in set(wirelist) :
        a = n - i
        answer.append(abs(a - i))

    return min(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/86971