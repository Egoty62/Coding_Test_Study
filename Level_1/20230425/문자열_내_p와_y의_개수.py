# 문자열 s를 소문자 또는 대문자로 만듦
    # 그 후 count()를 사용하여 수가 다르면 false 반환

def solution(s):
    answer = s.lower()
    if answer.count('p') != answer.count('y') :
        return False

    return True