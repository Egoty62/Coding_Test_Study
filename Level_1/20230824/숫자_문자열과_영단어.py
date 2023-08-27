def solution(s):
    eng_to_num = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    answer = ''
    temp = ''
    for i in s :
        if i.isdigit() :
            answer += i
        else :
            temp = temp + i
            if temp in eng_to_num :
                answer += eng_to_num[temp]
                temp = ''
    return int(answer)

# replace도 활용 가능함