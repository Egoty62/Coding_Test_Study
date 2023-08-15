# 탐욕법 알고리즘 : '현재' 상황에서 가장 좋은 것(최선의 선택)을 고르는 알고리즘

def solution(n, lost, reserve):
    tmp = []
    reserve.sort()
    for i in reserve :
        if i in lost :
            tmp.append(i)

    for i in tmp :
        reserve.remove(i)
        lost.remove(i)

    for i in reserve :
        if i - 1 in lost :
            lost.remove(i - 1)
        elif i + 1 in lost :
            lost.remove(i + 1)

    return n - len(lost)

def solution2(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    reserve_list = [i for i in reserve if i not in lost]
    lost_list = [j for j in lost if j not in reserve]

    for i in reserve_list :
        if i - 1 in lost_list :
            lost_list.remove(i - 1)
        elif i + 1 in lost_list :
            lost_list.remove(i + 1)

    return n - len(lost_list)