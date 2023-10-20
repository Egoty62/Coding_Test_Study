def solution(phone_book):
    
    pb = {k : 0 for k in phone_book}
    
    for i in phone_book :
        temp = ''
        for j in i :
            temp += j
            if temp in pb and temp != i :
                return False
    
    return True

# https://school.programmers.co.kr/learn/courses/30/lessons/42577