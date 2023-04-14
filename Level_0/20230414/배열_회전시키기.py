# 배열을 * 2 함
    # 그 후 'left'면 배열[1]부터 시작
    # 그 후 'right'면 배열[n-1]부터 시작

def solution(numbers, direction):
    answer_list = numbers * 2
    n = len(numbers)
    return answer_list[1 : n + 1] if direction == 'left' else answer_list[n - 1 : 2 * n - 1]