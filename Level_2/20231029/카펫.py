def solution(brown, yellow):
    n = brown + yellow
    for i in range(2, int(n ** (1/2)) + 1) :
        if n % i == 0 :
            j = n // i
            if (j + i - 2) * 2 == brown :
                return [j, i]
    return

# https://school.programmers.co.kr/learn/courses/30/lessons/42842