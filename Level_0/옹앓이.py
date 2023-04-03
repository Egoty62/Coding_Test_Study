def solution(babbling):
    list_babbling = ["aya", "ye", "woo", "ma"]
    list_answer = []
    answer = 0
    
    list_1 = [i for i in list_babbling]
    list_2 = [i + j for i in list_babbling for j in list_babbling if i != j]
    list_3 = [i + j + k for i in list_babbling for j in list_babbling for k in list_babbling if i != j and j != k and k != i]
    list_4 = [i + j + k + l for i in list_babbling for j in list_babbling for k in list_babbling for l in list_babbling if i != j and i != k and i != l and j != k and j != l and k != l]
    
    for n in list_1 :
        list_answer.append(n)
    for n in list_2 :
        list_answer.append(n)
    for n in list_3 :
        list_answer.append(n)
    for n in list_4 :
        list_answer.append(n)

    for _ in babbling :
        if _ in list_answer :
            answer += 1
    return answer