def solution(s):
    answer = []
    word = ''
    for i in s :
        a = word.find(i)
        if a != -1 :
            a += 1
        word = i + word
        answer.append(a)
        
    return answer