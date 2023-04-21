# 문자열의 길이가 짝수면 가운데 두 글자를 뽑아야 함
# 문자열의 길이가 홀수면 가운데 한 글자를 뽑아야 함
# 문자열 슬라이싱 활용

def solution(s):
    a = len(s)
    if a % 2 == 0 :
        return s[a // 2 - 1 : a // 2 + 1]
    else :
        return s[a // 2]