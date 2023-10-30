from collections import deque

def solution(board) :
    answer = 0
    board1 = []
    board1.append('D' * (len(board[0]) + 2))
    for i in board :
        temp = 'D' + i + 'D'
        board1.append(temp)
    board1.append('D' * (len(board[0]) + 2))
    board2 = [list(i) for i in board1]
    visited = [[-1 for j in range(len(board2[0]))] for i in range(len(board2))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()

    for i in board2 :
        for j in i :
            if j == 'R' :
                idx_a = board2.index(i)
                idx_b = i.index(j)
                visited[idx_a][idx_b] = 0
                queue.append([idx_a, idx_b])
            if j == 'G' :
                goal_a = board2.index(i)
                goal_b = i.index(j)
    
    while queue :
        idxa, idxb = queue.popleft()
        n = visited[idxa][idxb]
        for da, db in directions :
            a, b = idxa, idxb
            while board2[a][b] != 'D' :
                a += da
                b += db
            a -= da
            b -= db
            if visited[a][b] == -1 :
                queue.append([a, b])
                visited[a][b] = n + 1

    return visited[goal_a][goal_b]

# https://school.programmers.co.kr/learn/courses/30/lessons/169199

# 오타 제발 잘 보기...
    # 깊은복사 시도해보고 이것저것 다 시도해봤는데 안 됐던 이유가 오타로 인한 IndexError