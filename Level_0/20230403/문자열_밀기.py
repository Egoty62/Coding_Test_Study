def solution(A, B):
    list_a = list(A)
    answer = 0
    n = len(list_a)
    
    for i in range(n) :
        if "".join(list_a) == B : break
        temp = []
        temp.append(list_a[-1])
        for j in range(n - 1) :
            temp.append(list_a[j])
        list_a = temp
        answer += 1
        
    if "".join(list_a) == B :
        return answer
    else :
        return -1