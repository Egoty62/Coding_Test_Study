# 총 3가지 선분
    # 첫 번째 선분과 두 번째 선분
    # 첫 번째 선분과 세 번째 선분
    # 두 번째 선분과 세 번째 선분
        # 위 세 가지 케이스에서 겹치는 부분 찾아서 새로운 이차원 리스트로 만들기
# set, range 써서 합집합 만들면 될 거 같음

def solution(lines):
    a = set(range(lines[0][0], lines[0][1]))
    b = set(range(lines[1][0], lines[1][1]))
    c = set(range(lines[2][0], lines[2][1]))
    return len((a & b) | (b & c) | (c & a))