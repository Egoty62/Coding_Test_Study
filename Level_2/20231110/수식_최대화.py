from itertools import permutations as perm

def solution(expression):
    answer = []
    operator = ('-', '*', '+')
    numlist = expression.replace('-', '+').replace('*', '+').split('+')
    operstr = ''
    for i in expression :
        if i.isdigit() == False :
            operstr = operstr + i
    

    def calc(list_, operstr_, tuple_) :
        opernum = {oper : expression.count(oper) for oper in operator}
        operlist_ = list(operstr_)
        numlist_ = [i for i in list_]
        for i in tuple_ :
            while opernum[i] > 0 :
                a = operlist_.index(i)
                numlist_[a] = '(' + numlist_[a] + operlist_[a] + numlist_[a + 1] + ')'
                numlist_.pop(a + 1)
                operlist_.pop(a)
                opernum[i] -= 1
        answer.append(abs(eval(''.join(numlist_))))

        return
    for i in perm(operator) :
        calc(numlist, operstr, i)
    

    return max(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/67257