# str로 바꾸고, int형으로 다시 리스트로 만듦

def solution(n):
    return [int(str(n)[-i]) for i in range(1, len(str(n)) + 1)]