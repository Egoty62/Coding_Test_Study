# 내림차순으로 sorted()를 구한 후, (index) + 1을 반환

def solution(emergency):
    answer = sorted(emergency, reverse = True)
    return [answer.index(emergency[i]) + 1 for i in range(len(emergency))]