def solution(bin1, bin2):
    while len(bin1) < 11 : bin1 = '0' + bin1
    while len(bin2) < 11 : bin2 = '0' + bin2
    list_answer = [x + y for x, y in zip(map(int, list(bin1)), map(int, list(bin2)))]
    for i in range(-1, -12, -1) :
        while list_answer[i] >= 2 :
            list_answer[i] -= 2
            list_answer[i - 1] += 1
    while list_answer[0] == 0 :
        list_answer.pop(0)
    return ''.join(map(str, list_answer))

print(solution('1', '1111111111'))