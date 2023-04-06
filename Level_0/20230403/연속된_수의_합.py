def solution(num, total):
    if int(num) % 2 == 1 :
        answer = [i for i in range((total // num) - (num // 2), (total // num) + (num // 2 + 1))]
    else :
        answer = [i for i in range((total // num + 1) - (num // 2), (total // num + 1) + (num // 2))]
    return answer