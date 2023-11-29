def solution(game_board, table):
    answer = 0
    n = len(table)
    route = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    tablevisited = set()
    stack = []

    def rotate(array) :
        rotatearray = [list(i) for i in zip(*array[::-1])]
        return rotatearray
    
    def findblock(stack, array, visited, num_, list_) :
        while stack :
            temp = stack[-1]
            i, j = temp[0], temp[1]
            for a, b in route :
                if i + a >= 0 and i + a < n and j + b >= 0 and j + b < n :
                    if (i + a, j + b) not in visited :
                        if array[i + a][j + b] == num_ :
                            stack.append((i + a, j + b))
                            list_.append((i + a, j + b))
                            visited.add((i + a, j + b))
            if temp == stack[-1] :
                stack.pop()
            
        return
    
    def makepart(list_) :
        listi = [i[0] for i in list_]
        listj = [i[1] for i in list_]
        maxi, mini, maxj, minj = max(listi) + 1, min(listi), max(listj) + 1, min(listj)
        partlist = [[1 if (i, j) in list_ else 0 for j in range(minj, maxj)] for i in range(mini, maxi)]
        return partlist
    
    def match(list1, list2) :
        if list1 == list2 :
            for a, b in gameboardlist :
                game_board[a][b] = 1
            for c, d in tablelist :
                table[c][d] = 0
            return True
        else :
            return False
    
    for i in range(n) :
        for j in range(n) :
            if table[i][j] == 1 and (i, j) not in tablevisited :
                stack.append((i, j))
                tablevisited.add((i, j))
                tablelist = [(i, j)]
                findblock(stack, table, tablevisited, 1, tablelist)
                gameboardvisited = set()
                gameboardbull = False
                for k in range(n) :
                    for l in range(n) :
                        if game_board[k][l] == 0 and (k, l) not in gameboardvisited :
                            stack.append((k, l))
                            gameboardvisited.add((k, l))
                            gameboardlist = [(k, l)]
                            findblock(stack, game_board, gameboardvisited, 0, gameboardlist)
                            if len(gameboardlist) == len(tablelist) :
                                gameboardrect = makepart(gameboardlist)
                                tablerect = makepart(tablelist)
                                for count in range(4) :
                                    if count == 0 :
                                        bull = match(tablerect, gameboardrect)
                                        if bull :
                                            answer += len(tablelist)
                                            gameboardbull = True
                                            break
                                    else :
                                        tablerect = rotate(tablerect)
                                        bull = match(tablerect, gameboardrect)
                                        if bull :
                                            answer += len(tablelist)
                                            gameboardbull = True
                                            break
                            else : continue
                        if gameboardbull : break
                    if gameboardbull : break

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/84021