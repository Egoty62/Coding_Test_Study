# from itertools import combinations 활용

from itertools import combinations

def practice(balls, share):
    return len(list(combinations(list(range(balls)), share)))
# 이렇게 하면 시간 초과(10000ms)

# 조합 공식 사용(n! / ((n-r)! * r!))
from math import factorial

def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))
# math를 import 하지 않고 factorial 함수를 만들어서 적용시켜도 가능(재귀함수 형식)

# 다른 사람의 풀이
import math

def study(balls, share):
    return math.comb(balls, share)