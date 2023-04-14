# 짝수, 홀수를 따로 구분하고 개수 반환

def solution(num_list):
    return [len([o for o in num_list if o % 2 == 0]), len([e for e in num_list if e % 2 != 0])]