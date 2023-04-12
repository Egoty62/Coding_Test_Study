# keyinput의 원소에 따라 좌표를 변경
    # if 좌표의 끝 부분에 있으면 행동을 취소한 것처럼 보이게 하기

def solution(keyinput, board):
    up = board[1] // 2
    down = 0 - up
    right = board[0] // 2
    left = 0 - right
    answer = [0, 0]
    for i in keyinput :
        if i == 'left' :
            answer[0] -= 1
            if answer[0] <= left :
                answer[0] = left
        elif i == 'right' :
            answer[0] += 1
            if answer[0] >= right :
                answer[0] = right
        elif i == 'up' :
            answer[1] += 1
            if answer[1] >= up :
                answer[1] = up
        elif i == 'down' :
            answer[1] -= 1
            if answer[1] <= down :
                answer[1] = down
            
    return answer