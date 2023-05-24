# 입력된 수의 상태에 따라 처리 방식이 다름
    # 짝수라면 2로 나눔
    # 홀수라면 3을 곱하고 1로 더함
# 1이 될 때 까지 위 과정 반복

# 1이 되기까지 위 과정을 반복한 횟수를 반환
    # 입력된 수가 1이라면 0 반환
    # 과정이 500번 반복되기까지 1이 안 되면 -1 반환

def collatz(num) :
    result = 0
    while num != 1 :
        if num % 2 == 0 :
            num /= 2
        else :
            num = num * 3 + 1
        result += 1
    return -1 if result > 500 else result

# 간단하게 콜라츠 추측(위 과정)을 직접 진행함
    # 더 쉽게 푸는, result 값만 구하는 방법은 없을까?