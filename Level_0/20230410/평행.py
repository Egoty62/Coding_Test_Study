# 이차원 리스트의 맨 처음 값에 2, 3, 4번째 값을 각 비교
    # for, range
        # 사용 안 해도 됨
# 비교할 때마다 선택되지 않은 두 리스트끼리 비교
    # if i == ~~
# 기울기만 일치하면 됨
    # 두 개의 리스트에서 (두 번째 값 차이) / (첫 번째 값 차이) 가 일치

def solution(dots):
    if (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]) : return 1
    elif (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]) : return 1
    elif (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]) == (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0]) : return 1
    else : return 0