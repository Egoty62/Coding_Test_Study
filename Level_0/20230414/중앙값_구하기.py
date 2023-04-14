# sorted() 한 다음, len()을 사용하여 중앙 인덱스를 가진 원소 반환

def solution(array):
    return sorted(array)[len(array) // 2]
# sort()를 쓰면 len(array)가 NoneType이 됨