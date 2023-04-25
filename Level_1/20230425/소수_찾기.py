# 에라토스테네스의 체 알고리즘 사용
# 약수의 기준이므로 math.sqrt(n)이하의 자연수만 체로 걸러내면 됨
    # n ** (1 / 2) 사용하기

def solution(n):
    answer = [True] * (n + 1)
    for i in range(2, int(n ** (1 / 2)) + 1) :
        if answer[i] == True :
            for j in range(i + i, n + 1, i) :
                answer[j] = False
    return len([i for i in range(2, n + 1) if answer[i] == True])

# 다른 사람의 풀이
def study(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
# set를 사용하여 IndexError가 나지 않음 (차집합)

# 풀이 활용
def solution2(n : int) :
    answer = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1) :
        answer -= set(range(i + i, n + 1, i))
    return len(answer)

# set를 활용하는 것보다 True, False를 활용하는 가장 첫 번째의 코드가 실행시간이 더 짧음