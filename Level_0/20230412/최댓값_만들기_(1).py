# numbers 안에 있는 수는 모두 양수이므로 sort 후 마지막 두 수를 곱하기

def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]