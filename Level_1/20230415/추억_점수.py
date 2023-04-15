# {name : yearning}인 딕셔너리를 생성
# sum(), 리스트 컴프리헨션을 사용하여 결과 반환
    # defaultdict를 이용하여 KeyError가 나는 것을 방지

from collections import defaultdict

def solution(name, yearning, photo):
    ny_dict = defaultdict(int, {k : v for k, v in zip(name, yearning)})
    return [sum([ny_dict[i] for i in photo[j]]) for j in range(len(photo))]