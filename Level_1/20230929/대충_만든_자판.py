def solution(keymap, targets):
    answer = []
    for i in targets :
        a = 0
        for j in i :
            try :
                a += min([key.find(j) + 1 for key in keymap if key.find(j) != -1])
            except ValueError :
                a = -1
                break
        answer.append(a)
    return answer