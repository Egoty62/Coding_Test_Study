from heapq import heappush, heappop

def solution(operations):
    answer = []
    n = 0
    for i in operations :
        a, b = i.split()
        if a == 'I' :
            heappush(answer, int(b))
            n += 1
        elif a == 'D' :
            if n == 0 : continue
            else :
                if b == '1' :
                    answer.remove(max(answer[n // 2 :]))
                    n -= 1
                elif b == '-1' :
                    heappop(answer)
                    n -= 1
    return [max(answer[n // 2 :]), answer[0]] if answer else [0, 0]

# https://school.programmers.co.kr/learn/courses/30/lessons/42628