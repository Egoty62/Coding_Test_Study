def solution(a, b, g, s, w, t):
    maxtime = 4 * 10 ** 14
    mintime = 0
    while maxtime >= mintime :
        midtime = (maxtime + mintime) // 2
        gs = {'g' : 0, 'smin' : 0, 'smax' : 0}
        weight = [(midtime // (i * 2) + 1) * j if midtime % (i * 2) >= i else (midtime // (i * 2)) * j for i, j in zip(t, w)]
        for i in range(len(weight)) :
            if weight[i] > g[i] :
                m = weight[i]
                gs['g'] += g[i]
                m -= g[i]
                gs['smin'] += min(m, s[i])
            else : gs['g'] += weight[i]

            gs['smax'] += min(weight[i], s[i])

        if gs['g'] >= a and gs['smax'] >= b and (gs['g'] + gs['smin']) >= (a + b) :
            maxtime = midtime - 1
        else : mintime = midtime + 1
        
    return mintime

# https://school.programmers.co.kr/learn/courses/30/lessons/86053