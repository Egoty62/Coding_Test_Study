# 0 ~ 10 팩토리얼 리스트를 만들고 조건에 만족하는 인덱스를 반환

def solution(n):
    answer = [0, 1, 2, 2 * 3, 2 * 3 * 4, 2 * 3 * 4 * 5, 2 * 3 * 4 * 5 * 6, 2 * 3 * 4 * 5 * 6 * 7, 2 * 3 * 4 * 5 * 6 * 7 * 8, 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9, 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10]
    return answer.index(max(i for i in answer if i <= n))


def solution2(n) :
    from functools import reduce
    answer = [reduce(lambda x, y : x * y, [i for i in range(1, j)]) for j in range(2, 12)]
    return answer.index(max(i for i in answer if i <= n)) + 1