# range()로 리스트를 만든 뒤 sum()
# a, b의 대소관계는 정해져 있지 않음
    # max(), min()으로 대소관계 구분하기

def solution(a, b):
    return sum([i for i in range(min(a, b), max(a, b) + 1)])