def solution(cards):
    temp1 = []
    num_list = []
    temp2 = []
    
    for i in cards :
        j = i
        while j not in temp2 :
            temp1.append(j)
            temp2.append(j)
            j = cards[j - 1]
        num_list.append(len(temp1))
        temp1 = []
           
    num_list.sort()
    print(num_list)
    
    return num_list[-1] * num_list[-2]

# https://school.programmers.co.kr/learn/courses/30/lessons/131130