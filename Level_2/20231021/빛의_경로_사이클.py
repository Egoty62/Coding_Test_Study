arrow = ['d', 'l', 'u', 'r']

def direction(di, state) :
    if state == 'S' :
        wayout = di
    elif state == 'L' :
        wayout = di - 1
        if wayout < 0 : wayout += 4
    else :
        wayout = di + 1
        if wayout >= 4 : wayout -= 4
        
    return wayout

def go(di, a, b) :
    i, j = a, b
    if arrow[di] == 'd' :
        i += 1
        if i >= n : i -= n
    elif arrow[di] == 'l' :
        j -= 1
        if j < 0 : j += m
    elif arrow[di] == 'u' :
        i -= 1
        if i < 0 : i += n
    elif arrow[di] == 'r' :
        j += 1
        if j >= m : j -= m

    return i, j

def solution(grid) :
    answer = []
    global n, m
    n, m = len(grid), len(grid[0])

    grid_2 = [list(i) for i in grid]

    all_of_light_start = {(i, j) : [] for j in range(m) for i in range(n)}

    for i in range(n) :
        for j in range(m) :
            for k in arrow :
                if k in all_of_light_start[(i, j)] : continue
                count = 0
                x, y = i, j
                di = arrow.index(k)
                state = grid_2[x][y]
                while 1 :
                    if count == 0 :
                        all_of_light_start[(x, y)].append(arrow[di])
                        x, y = go(di, x, y)
                        count += 1
                        state = grid_2[x][y]
                    else :
                        if arrow[direction(di, state)] in all_of_light_start[(x, y)] : break
                        di = direction(di, state)
                        all_of_light_start[(x, y)].append(arrow[di])
                        x, y = go(di, x, y)
                        count += 1

                        state = grid_2[x][y]

                answer.append(count)

    return sorted(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/86052