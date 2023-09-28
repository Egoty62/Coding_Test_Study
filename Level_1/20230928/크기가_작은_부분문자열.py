def solution(t, p):
    temp = [int(t[i : i + len(p)]) for i in range(len(t)) if len(t[i : i + len(p)]) == len(p)]
    return sum([1 for i in temp if i <= int(p)])