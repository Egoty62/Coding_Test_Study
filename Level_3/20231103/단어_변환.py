def solution(begin, target, words):
    if target not in words : return 0
    else :
        answer = []
        stack = []
        n = len(begin)
        visited = {i : [] for i in words}
        visited[begin] = []
        stack.append(begin)
        while len(stack) :
            last = stack[-1]
            if last == target :
                answer.append(len(stack) - 1)
            else :
                for k in [i for i in words if i not in stack] :
                    print(k, stack)
                    if k in visited[stack[-1]] :
                        stack.pop()
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

            #print(stack)
    return min(answer) if answer else 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))