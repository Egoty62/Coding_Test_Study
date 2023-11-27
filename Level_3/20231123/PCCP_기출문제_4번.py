def solution(maze):
    answer = []
    n, m = len(maze), len(maze[0])
    redset = set()
    blueset = set()
    newredset = {}
    newblueset = {}

    for i in range(n) :
        for j in range(m) :
            if maze[i][j] == 1 :
                red = (i, j)
                redset = {(i, j)}
            if maze[i][j] == 2 :
                blue = (i, j)
                blueset = {(i, j)}
            if maze[i][j] == 3 :
                reddest = (i, j)
            if maze[i][j] == 4 :
                bluedest = (i, j)

    def tree(loc, goal) :
        i, j = loc
        treelist = []

        if loc == goal : treelist.append(goal)
        else :
            for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] :
                if a >= 0 and a < n and b >= 0 and b < m and maze[a][b] != 5 :
                    treelist.append((a, b))
        return treelist

    def dfs(red, blue, count, redset, blueset) :
        nonlocal newredset
        nonlocal newblueset
        if count > n * m + 1:
            return
        elif red == reddest and blue == bluedest :
            answer.append(count - 1)
            return
        else :
            redtree = tree(red, reddest)
            bluetree = tree(blue, bluedest)
            for a, b in redtree :
                for c, d in bluetree :
                    if not ((a, b) in redset or (c, d) in blueset or (a, b) == (c, d) or ((a, b), (c, d)) == (blue, red)) :
                        if (a, b) == reddest :
                            newblueset = blueset.union({(c, d)})
                        elif (c, d) == bluedest :
                            newredset = redset.union({(a, b)})
                        else :
                            newredset = redset.union({(a, b)})
                            newblueset = blueset.union({(c, d)})
                        dfs((a, b), (c, d), count + 1, newredset, newblueset)
                        
    dfs(red, blue, 1, redset, blueset)
    
    return min(answer) if answer else 0

# https://school.programmers.co.kr/learn/courses/30/lessons/250134