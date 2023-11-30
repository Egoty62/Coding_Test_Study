def solution(n):
    answerset = set()
    bracket = ''
    bracketnum = {i : 0 for i in ('(', ')')}

    def dfs(num, str_, dict_) :
        if num == n * 2 :
            answerset.add(str_)
        elif dict_['('] == dict_[')'] :
            str_ += '('
            dict_['('] += 1
            dfs(num + 1, str_, dict_)
        elif dict_['('] == n :
            str_ += ')'
            dict_[')'] += 1
            dfs(num + 1, str_, dict_)
        else :
            dict1 = {i : j for i, j in dict_.items()}
            dict2 = {i : j for i, j in dict_.items()}
            dict1[')'] += 1
            dict2['('] += 1
            dfs(num + 1, str_ + ')', dict1)
            dfs(num + 1, str_ + '(', dict2)
                
    dfs(0, bracket, bracketnum)

    return len(answerset)

# 카탈란 수를 활용하여 풀 수도 있음

from math import factorial
def study1(n) :
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))

def study2(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            # n=2 -> dp[2] = (dp[1] * dp[0]) + (dp[0] * dp[1])
            # n=3 -> dp[3] = (dp[1] * dp[0]) + (dp[0] * dp[1]) + (dp[2] * dp[0]) + (dp[1] * dp[1]) + (dp[0] * dp[2])
            dp[i] += dp[i-j] * dp[j-1]
    return dp[n]

# https://school.programmers.co.kr/learn/courses/30/lessons/12929