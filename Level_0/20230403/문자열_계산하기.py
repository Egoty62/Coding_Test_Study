def solution(my_string):
    return eval(my_string)  # 보안문제

def solution2(my_string):
    a = my_string.split()
    result = int(a[0])
    for i in range(len(a)) :
        if i % 2 == 1 :
            if a[i] == '+' :
                result += int(a[i+1])
            elif a[i] == '-' :
                result -= int(a[i+1])
    return result