def solution(number, limit, power):
    temp = []
    for i in range(1, number + 1) :
        root = i ** (1 / 2)
        divisor = 0
        for j in range(1, int(root) + 1) :
            if i % j == 0 :
                divisor += 2
        if root == int(root) :
            divisor -= 1
        temp.append(divisor)
        
    return sum([i if i <= limit else power for i in temp])