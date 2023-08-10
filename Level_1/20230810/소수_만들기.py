from itertools import combinations

def solution(nums):
    answer = 0
    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            for k in range(j + 1, len(nums)) :
                a = nums[i] + nums[j] + nums[k]
                l = 2
                while l <= a // 2 :
                    if a % l == 0 : break
                    else : l += 1
                    if l > a // 2 : answer += 1
    return answer

def solution2(nums) :
    answer = 0
    for i in combinations(nums, 3) :
        a = sum(i)
        for j in range(2, a // 2) :
            if a % j == 0 : break
        else : answer += 1
    return answer
# for - else문