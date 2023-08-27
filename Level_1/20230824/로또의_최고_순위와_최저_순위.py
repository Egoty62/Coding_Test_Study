def solution(lottos, win_nums):
    answer = sum([(i in win_nums) for i in lottos])
    result = [7 - (answer + lottos.count(0)), 7 - answer]
    for i in range(2) :
        if result[i] > 6 :
            result[i] = 6
    return result