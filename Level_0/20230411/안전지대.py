# 1이 있는 좌표의 주변을 0, 1이 아닌 다른 것으로 바꾸고 0의 개수를 return
    # 위, 아래
        # if [i, j] == 1, [[m, n] for m in range(i - 1, i + 2) for n in range(j - 1, j + 2)]
            # 만약 1 또는 이미 바뀐 숫자라면 continue
# 배열을 초과하는 index는 try-except로 해결하면 됨

def solution(board):
    a = board
    for i in range(len(board)) :
        for j in range(len(board)) :
            if a[i][j] == 1 :
                for k in [x for x in range(i - 1, i + 2) if x > -1] :
                    for l in [y for y in range(j - 1, j + 2) if y > -1] :
                        try :
                            if a[k][l] == 0 :
                                a[k][l] = 2
                        except IndexError : continue
    return sum([a[i].count(0) for i in range(len(board))])

# a[-1]이 배열 a의 가장 마지막 값을 가리키는 등 음수 인덱스에 대한 고려가 늦었음