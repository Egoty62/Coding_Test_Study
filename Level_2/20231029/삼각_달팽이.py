# 무조건 첫 행은 1, 2번째 행은 2
# 마지막 n개의 숫자는 n, n+1, ... 2n - 1

# -3 씩 재귀함수 돌리기
# insert 사용하기

def solution(n):
    answer = []
    snaildict = {i : [] for i in range(1, n + 1)}

    def snail(int_, dimension_, a_, b_) :
        if dimension_ == 1 :
            snaildict[a_].append(int_)
            
        elif dimension_ == 2 :
            snaildict[a_].append(int_)
            snaildict[a_ + 1].append(int_ + 1)
            snaildict[a_ + 1].append(int_ + 2)

        elif dimension_ == 3 :
            snaildict[a_].append(int_)
            snaildict[a_ + 1].append(int_ + 1)
            snaildict[a_ + 2].append(int_ + 2)
            snaildict[a_ + 2].append(int_ + 3)
            snaildict[a_ + 2].append(int_ + 4)
            snaildict[a_ + 1].append(int_ + 5)
            
        else :
            for i, j in zip(range(a_, a_ + dimension_ - 1), range(int_, int_ + dimension_ - 1)) :
                snaildict[i].append(j)
            snail(int_ + dimension_ * 3 - 3, dimension_ - 3, a_ + 2, b_ -1)
            for i, j in zip(range(a_ + 1, b_), range(int_ + 3 * dimension_ - 4, 2 * dimension_ - 1, -1)) :
                snaildict[i].append(j)
            for i in range(int_ + dimension_ - 1, int_ + dimension_ * 2 - 1) :
                snaildict[b_].append(i)

        return
    
    snail(1, n, 1, n)
    for i in range(1, n + 1) :
        answer.extend(snaildict[i])

    return answer
    
# https://school.programmers.co.kr/learn/courses/30/lessons/68645