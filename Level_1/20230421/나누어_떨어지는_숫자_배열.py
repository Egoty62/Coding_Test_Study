# sorted() 함수 사용
# 리스트 컴프리헨션

def solution(arr, divisor):
    return [i for i in sorted(arr) if i % divisor == 0] if len([i for i in sorted(arr) if i % divisor == 0]) != 0 else [-1]

# 다른 사람의 풀이

def study(arr, divisor) :
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
# or 사용법 : 앞의 것이 참이 아닐 때 뒤의 것을 반환