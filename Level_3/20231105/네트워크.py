def solution(n, computers):
    answer = 0
    visited = {i : False for i in range(n)}
    stack = []
    for i in range(n) :
        if visited[i] == True : continue
        else :
            stack.append(i)
            while stack :
                last = stack[-1]
                if visited[last] == True :
                    stack.pop()
                else :
                    for j in range(n) :
                        if stack[-1] == j or visited[j] == True : continue
                        elif computers[stack[-1]][j] == 1 and j not in stack :
                            stack.append(j)
                    if last == stack[-1] :
                        visited[last] = True

        answer += 1

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/43162