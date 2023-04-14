# n 이하의 자연수 중 해당 수 제외 나머지 수로 나눴을 때 나머지가 0이 되면 합성수 + 1

def solution(n):
    k = 3
    answer = 0
    if n == 1 or n == 2 : return 0
    else :
        while k <= n :
            if k == 1 : continue
            else :
                for i in range(2, k) :
                    if k % i == 0 :
                        answer += 1
                        break
            k += 1
    return answer