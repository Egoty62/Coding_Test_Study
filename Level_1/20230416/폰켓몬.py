# 배열 안의 원소는 중복될 수 있음
# 원소가 중복되는 배열 속에서 절반을 뽑아야 함 (배열의 크기는 항상 짝수)
# 이 때, 원소의 '종류'가 가장 많은 경우의 원소 개수를 반환해야함

# 배열에서 원소를 뽑을 때의 가짓수를 만듦
    # math.comb 또는 조합 공식을 그대로 사용
        # 문제의 특성 상 조합을 사용하면 배열이 커질 경우 시간이 엄청나게 소모됨
# 원소의 종류만 출력해야 함
    # set 사용

# 배열의 크기를 len()을 이용하여 저장
    # 그 후 set를 이용해 원소의 중복이 없게 배열 압축
        # if len(set)가 기존 배열의 크기 / 2 보다 작으면 len(set)를 반환
        # elif len(set)가 기존 배열의 크기 / 2 보다 크면 기존 배열의 크기 / 2를 반환
        # elif 같으면 그냥 둘 중 아무거나 반환

def solution(nums):
    n = len(nums) // 2
    nums_set = set(nums)
    return len(nums_set) if len(nums_set) < n else n

# min을 사용해도 가능

def solution2(nums) :
    return min(len(nums) // 2, len(set(nums)))