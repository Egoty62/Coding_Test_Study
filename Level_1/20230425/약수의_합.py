# 리스트 컴프리헨션 후 sum() 하기

def solution(n):
    return sum([i + n // i if i != n // i else i for i in range(1, int(n ** 0.5) + 1) if n % i == 0])

# 제곱수 고려, 약수의 관계에 따라 루트n까지만 검사해도 됨
    # 수행 시간 단축을 위해 루트n까지만 검사했음 

def example(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])
# 이렇게 하면 첫 번째 코드에 비해 시간이 엄청 걸림