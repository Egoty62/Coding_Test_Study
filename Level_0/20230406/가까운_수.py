def solution(array, n):
    gap_minimum = n + 100
    for i in array :
        if i - n < 0 :
            gap = n - i
        else :
            gap = i - n
        if gap_minimum > gap :
            gap_minimum = gap
            answer = i
        elif gap_minimum == gap :
            if answer > i :
                answer = i
    return answer

# 다른 사람의 풀이
asd = lambda a, n : sorted(a, key = lambda x : (abs(x - n), x))[0]  # (abs(x -n), x) : x의 값까지 고려 (더 작은 것을 return 해야 하기 때문)
