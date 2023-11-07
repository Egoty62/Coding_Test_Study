def solution(n, edges):
    link = {i : {} for i in range(1, n + 1)}
    distance = {i : -1 for i in range(1, n + 1)}

    for a, b in edges :
        link[a][b] = 1
        link[b][a] = 1

    distance[1] = 0

    queue = []
    queue.append(1)
    while queue :
        a = queue.pop(0)
        if link[a] :
            for i in link[a] :
                if distance[i] == -1 :
                    distance[i] = distance[a] + 1
                    queue.append(i)
                    num = distance[i]
                else : continue
    


    return len([1 for i in distance.values() if i == num])

# https://school.programmers.co.kr/learn/courses/30/lessons/49189