def solution(begin, target, words):
    if target not in words : return 0
    else :
        answer = []
        stack = []
        n = len(begin)
        visited = {i : [] for i in words}
        visited[begin] = []
        stack.append(begin)
        while stack :
            last = stack[-1]
            if last == target :
                answer.append(len(stack) - 1)
            else :
                for k in [i for i in words if i not in stack] :
                    if k in visited[last] :
                        continue
                    else :
                        diff = 0
                        for j in range(n) :
                            if stack[-1][j] != k[j]:
                                diff += 1
                        if diff == 1 :
                            visited[stack[-1]].append(k)
                            stack.append(k)
            if last == stack[-1] :
                stack.pop()
            
    return min(answer) if answer else 0

# https://school.programmers.co.kr/learn/courses/30/lessons/43163