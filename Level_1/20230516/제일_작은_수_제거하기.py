# 정수로 이루어진 배열에서 가장 작은 원소를 뺀 배열을 반환
    # 크기가 1인 배열은 -1 반환
# min, remove 사용

def solution(arr):
    a = min(arr)
    arr.remove(a)
    return arr if len(arr) >= 1 else [-1]