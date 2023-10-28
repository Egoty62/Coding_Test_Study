# 다익스트라 알고리즘
# 첫 번째 구간 : 동승하는 구간 C
# 두 번째 구간 : 동승 도착지에서 A 도착지까지의 구간 A
# 세 번째 구간 : 동승 도착지에서 B 도착지까지의 구간 B

# C + A + B가 최소가 되는 값을 구하는 문제
    # C는 모든 구간이 될 수 있음
        # A, B는 출발(모든 구간)점에서 최소 거리의 합을 미리 구함
            # S -> C의 구간을 따로 구해서 A, B 값에 합해줌

# S에서 모든 구간으로 갈 때의 비용을 구하는 코드 ... (1)
    # 모든 구간에서 A로 갈 때의 비용을 구하는 코드
    # 모든 구간에서 B로 갈 때의 비용을 구하는 코드
        # 모든 구간에서 A, B로 갈 때의 비용의 합을 구하는 코드 ... (2)
            # (1) 값과 (2) 값을 합해서 최종적으로 비용이 적게 드는 값을 반환

def solution(n, s, a, b, fares):    # n : 노드 수, s : 출발지점, a : a 도착지점, b : b 도착지점

    path = {i : {j[0] : j[2] for j in fares if i == j[1]} for i in range(1, n + 1)}
    for i in fares :
        for j in range(1, n + 1) :
            if j == i[0] :
                path[j][i[1]] = i[2]
    cost_s = {i : -1 for i in range(1, n + 1)}
    cost_a = {i : -1 for i in range(1, n + 1)}
    cost_b = {i : -1 for i in range(1, n + 1)}
    cost_s[s] = 0
    
    def min_route(dict_, int_) :
        dict_[int_] = 0
        count = 0
        while count < n :
            for i in range(1, n + 1) :
                
                if dict_[i] == -1 : continue
                else :
                    for j in path[i] :
                        temp = dict_[i] + path[i][j]

                        if dict_[j] == -1 :
                            dict_[j] = temp
                        elif dict_[j] > temp :
                            dict_[j] = temp
                        else : continue
                    
            count += 1
        
        return (dict_)

    cost_s = min_route(cost_s, s)
    cost_a = min_route(cost_a, a)
    cost_b = min_route(cost_b, b)

    answer = [cost_a[i] + cost_b[i] + cost_s[i] for i in range(1, n + 1) if cost_a[i] != -1 and cost_b[i] != -1 and cost_s[i] != -1]

    return min(answer)

# 아래 코드는 heapq.heappush()를 사용한 코드
    # 문제를 직접 다 푼 뒤 본 다른 사람의 풀이 코드

import heapq

def study(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv

# https://school.programmers.co.kr/learn/courses/30/lessons/72413