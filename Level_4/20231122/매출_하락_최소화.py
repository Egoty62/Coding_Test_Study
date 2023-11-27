def solution(sales, links):
    cost = {i : [0, j] for i, j in zip(range(1, len(sales) + 1), sales)}
    team = {}
    visited = {i : False for i in range(1, len(sales) + 1)}

    for i, j in links :
        if i not in team :
            team[i] = [j]
        else :
            team[i].append(j)

    def dfs(num_, pnum_) :
        visited[num_] = True
        if num_ in team :
            for i in team[num_] :
                dfs(i, num_)
            cost[num_][0] = min([cost[j][1] for j in team[num_]])
            cost[num_][1] += min([min(cost[j]) for j in team[num_]])

        if pnum_ and all([visited[i] for i in team[pnum_]]) :        
            temp = sum([min(cost[j]) for j in team[pnum_]])
            for i in team[pnum_] :
                a = temp - min(cost[i])
                for j in range(2) :
                    cost[i][j] += a
    dfs(1, 0)
    return min(cost[1])

# https://school.programmers.co.kr/learn/courses/30/lessons/72416