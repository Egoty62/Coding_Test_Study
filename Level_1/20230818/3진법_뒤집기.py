def solution(n):
    trit = ''
    answer = 0
    temp = 0
    
    while n >= 3 :
        trit = str(n % 3) + trit
        n = n // 3
    trit = str(n) + trit
    
    for i in trit :
        answer += int(i) * 3 ** temp
        temp += 1
        
    return answer

def solution2(n):
    trit = ''
    while n != 0 :
        trit += str(n % 3)
        n = n // 3
    
    return int(trit, 3)