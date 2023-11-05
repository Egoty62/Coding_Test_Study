answer = []
hanoi = {k : [] for k in range(1, 4)}

def record_before(n, before, after) :
    c = 6 - before - after
    if n == 1 :
        answer.append([before, c])
    else :
        record_before(n - 1, before, c)
        answer.append([before, c])
        record_after(n - 1, before, c)

def record_after(n, before, after) :
    c = 6 - before - after
    if n == 1 :
        answer.append([c, after])
    else :
        record_before(n - 1, c, after)
        answer.append([c, after])
        record_after(n - 1, c, after)

def solution(n):

    before = 1
    after = 3
    record_before(n - 1, before, after)
    answer.append([1, 3])
    record_after(n - 1, before, after)
        
    return answer