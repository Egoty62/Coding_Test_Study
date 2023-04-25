# len()이 4 또는 6일 경우
    # isdigit()가 True면 True 반환

def solution(s):
    if len(s) == 4 or len(s) == 6 :
        if s.isdigit() :
            return True
    return False