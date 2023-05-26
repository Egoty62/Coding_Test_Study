# x를 숫자들로 쪼갠 새로운 리스트 생성
    # 그 리스트의 sum()을 구함
        # 그 후 나머지가 0일 때 true를 반환

def solution(x):
    x_list = [int(i) for i in str(x)]
    return True if x % sum(x_list) == 0 else False

def solution2(x) :
    x_list = [int(i) for i in str(x)]
    return x % sum(x_list) == 0