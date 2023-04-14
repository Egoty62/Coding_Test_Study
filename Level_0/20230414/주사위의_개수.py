# box의 각 원소를 n으로 나눴을 때의 몫을 곱해주기
   # reduce() 사용 

from functools import reduce
def solution(box, n):
    return reduce(lambda x, y : x * y, [i // n for i in box])