def solution(answers):
    answer = []
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a = 0
    b = 0
    c = 0
    for i in range(len(answers)) :
        if list_1[i % len(list_1)] == answers[i] :
            a += 1
        if list_2[i % len(list_2)] == answers[i] :
            b += 1
        if list_3[i % len(list_3)] == answers[i] :
            c += 1
    print(a, b, c)
    if a == max(a, b, c) : answer.append(1)
    if b == max(a, b, c) : answer.append(2)
    if c == max(a, b, c) : answer.append(3)
    return answer