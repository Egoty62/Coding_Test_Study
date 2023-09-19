from itertools import combinations as comb

def solution(number):
    number_sum = [sum(i) for i in list(comb(number, 3))]
    return number_sum.count(0)