def solution(sizes):
    result = max([max(i) for i in sizes]) * max([min(i) for i in sizes])
    return result