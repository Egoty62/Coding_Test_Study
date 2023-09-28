def solution(today, terms, privacies):
    answer = []
    pri = [i.split() for i in privacies]
    ter = {k : int(v) for k, v in [i.split() for i in terms]}
    pri_date = [[int(i), int(j), int(k)] for i, j, k in [l[0].split('.') for l in pri]]
    pri_list = [[k , ter[v]] for k, v in pri]
    today_int = [int(i) for i in today.split('.')]
    
    for i in range(len(pri)) :
        pri_date[i][1] += pri_list[i][1]
        while pri_date[i][1] > 12 :
            pri_date[i][0] += 1
            pri_date[i][1] -= 12
    
    for i in range(len(pri_date)) :
        if pri_date[i] <= today_int :
            answer.append(i + 1)

    return answer