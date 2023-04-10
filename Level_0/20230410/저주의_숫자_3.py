# 3의 배수, 3이 들어간 수를 쓰지 않음
    # [i for i in range(1, n * 2) if i % 3 != 0]
    # if '3' not in list(str(i))

def solution(n):
    a = [i for i in range(1, 200) if i % 3 != 0 and '3' not in list(str(i))]
    return a[n - 1]

# n의 최댓값이 100이라서 그 두 배인 200을 입력함