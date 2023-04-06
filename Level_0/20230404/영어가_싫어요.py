def solution(numbers):
    dict_number = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    temp = []
    list_answer = []
    answer = []
    for i in numbers :
        temp.append(i)
        if ''.join(temp) in dict_number.keys() :
            a = ''.join(temp)
            list_answer.append(dict_number[a])
            temp = []
    for j in list_answer :
        answer.append(str(j))
    return int(''.join(answer))