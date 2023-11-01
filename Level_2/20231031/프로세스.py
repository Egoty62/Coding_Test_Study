def solution(priorities, location):
    process = [i for i in range(len(priorities))]
    clear = []

    while priorities :
        max_p = max(priorities)
        a = priorities.pop(0)
        b = process.pop(0)
        if a == max_p :
            clear.append(b)
        else :
            priorities.append(a)
            process.append(b)

    return clear.index(location) + 1

# https://school.programmers.co.kr/learn/courses/30/lessons/42587