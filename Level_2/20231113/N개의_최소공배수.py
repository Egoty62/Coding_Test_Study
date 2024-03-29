import math

def solution(arr):
    for i in range(len(arr) - 1) :
        gcd = math.gcd(arr[i], arr[i + 1])
        answer = arr[i] * arr[i + 1] // gcd
        arr[i + 1] = answer
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12953