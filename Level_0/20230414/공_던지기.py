# 배열의 0번째 부터 2 * (k - 1)만큼 더함
    # 답이 배열의 크기보다 크면 작아질 때 까지 계속 빼줌
        # 나머지 구하기

def solution(numbers, k):
    return numbers[(2 * (k - 1)) % len(numbers)]