# 직사각형이므로 밑변 * 높이만 하면 됨
    # 리스트의 첫 번째 원소 기준으로 dots[0][0], dots[0][1]과 값이 같은 dots[i][0], dots[j][1] 찾고, 계산

def solution(dots):
    for i in dots :
        if i == dots[0] : continue
        else :
            if i[0] == dots[0][0] :
                height = abs(i[1] - dots[0][1])
            elif i[1] == dots[0][1] :
                base = abs(i[0] - dots[0][0])
            else : continue
    return height * base

def solution2(dots) :
    return abs((max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1]))