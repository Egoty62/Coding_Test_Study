# map 함수 사용

# 리스트 컴프리헨션 사용

def solution(numbers):
    return list(map(lambda x : x * 2, numbers))

def solution2(numbers) :
    return [i * 2 for i in numbers]