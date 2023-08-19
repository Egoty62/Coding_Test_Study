# 1, 4, 7, *, 3, 6, 9, #은 L, R이 고정 => 딕셔너리로 해결해보기
# l, r과 2, 5, 8, 0 키패드 사이의 거리를 구하는 코드가 필요
    # 숫자에서 3이 더해지거나 빠지면 거리 +1 (0 제외)
    # 숫자에서 1이 더해지거나 빠지면 거리 +1 (0 제외)
    # * => 7, * => 0은 거리 +1
    # # => 9, # => 0은 거리 +1
        # 위 조건들을 이용하여 l, r과의 거리 구하기
            # 거리가 더 짧은 쪽으로 문자열 추가, 거리가 같으면 hand 변수에 따라 문자열 추가

def solution(numbers, hand):
    l, r = 10, 12
    keypad = {1 : 'L', 4 : 'L', 7 : 'L', 10 : 'L', 3 : 'R', 6 : 'R', 9 : 'R', 12 : 'R'}
    rep = {0 : 11, '*' : 10, '#' : 12}
    answer = ''
    
    for i in numbers :
        if i in rep :
            i = rep[i]
        if i in keypad :
            answer += keypad[i]
            if keypad[i] == 'L' :
                l = i
            else :
                r = i
        else :
            l_dis = abs(i - l) // 3 + abs(i - l) % 3
            r_dis = abs(i - r) // 3 + abs(i - r) % 3
            if l_dis == r_dis :
                if hand == 'left' :
                    answer += 'L'
                    l = i
                else :
                    answer += 'R'
                    r = i
            elif l_dis < r_dis :
                answer += 'L'
                l = i
            else :
                answer += 'R'
                r = i
    return answer