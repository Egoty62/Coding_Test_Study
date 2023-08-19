from itertools import combinations as comb

def solution(numbers):
    return sorted(list(set([sum(i) for i in comb(numbers, 2)])))