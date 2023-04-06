def solution(sides):
    sum_sides = sum(sides)
    answer = 1
    for i in sides :
        if i * 2 < sum_sides : continue
        else : return 2
    return answer