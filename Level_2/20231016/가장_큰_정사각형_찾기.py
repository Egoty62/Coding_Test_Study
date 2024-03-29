# 다이나믹 프로그래밍
def solution(board):
    answer = 0
    if len(board) == 1 and len(board[0]) == 1 :
        return board[0][0]
    for i in range(1, len(board)) :
        for j in range(1, len(board[0])) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
            if answer < board[i][j] :
                answer = board[i][j]

    return answer ** 2