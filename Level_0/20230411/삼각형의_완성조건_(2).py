# 리스트 컴프리헨션으로 가능할 것 같음
# 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 작아야 함
    # Case 1. 주어진 리스트의 원소 중 큰 것이 가장 긴 변일 경우
        # max(sides) < min(sides) + integer
    # Case 2. 주어지지 않은 변의 길이가 가장 긴 변일 경우
        # integer < sum(sides)
    # 하나의 리스트 컴프리헨션으로 안 되면 extend() 사용
# 결과는 len()으로 해결

# [i for i in range(1, 2000) if max(sides) < min(sides) + i]
# [i for i in range(1, 2000) if i < sum(sides)]

def solution(sides):
    return len([i for i in range(1, 2000) if max(sides) < min(sides) + i and i < sum(sides)])