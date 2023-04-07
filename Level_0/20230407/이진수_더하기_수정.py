def solution(bin1, bin2):
    while len(bin1) < 20 : bin1 = '0' + bin1
    while len(bin2) < 20 : bin2 = '0' + bin2
    list_answer = [x + y for x, y in zip(map(int, list(bin1)), map(int, list(bin2)))]
    for i in range(-1, -12, -1) :
        while list_answer[i] >= 2 :
            list_answer[i] -= 2
            list_answer[i - 1] += 1
    while list_answer[0] == 0 :
        if len(list_answer) == 1 : break    # "0" + "0"의 경우에는 이 문장이 꼭 필요함
        list_answer.pop(0)
    return ''.join(map(str, list_answer))

def solution2(bin1, bin2) :
    answer = str(bin(int(bin1, 2) + int(bin2, 2)))
    return answer[2:]