def solution(triangle):
    n = len(triangle)
    
    for i in range(n - 1, -1, -1) :
        j = i - 1
        for k in range(i) :
            triangle[j][k] = max(triangle[j][k] + triangle[i][k], triangle[j][k] + triangle[i][k + 1])        
    return triangle[0][0]

# https://school.programmers.co.kr/learn/courses/30/lessons/43105