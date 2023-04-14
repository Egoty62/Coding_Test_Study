# 나머지가 존재하면 n // slice + 1, 나머지가 없으면 n // slice

def solution(slice, n):
    return n // slice + 1 if n % slice != 0 else n // slice