def solution(my_string):
    temp = []
    answer = []
    for i in my_string :
        if i in temp : continue
        else : 
            answer.append(i)
            temp.append(i)
    return ''.join(answer)

# 다른 사람의 풀이
def solution2(my_string):
    return ''.join(dict.fromkeys(my_string))    # 딕셔너리는 join 할 때 key만 결합시킴