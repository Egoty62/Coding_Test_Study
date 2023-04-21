# set는 할 수 없음
# 바로 뒤에 있는 것만 삭제하면 됨
    # 원소를 temp에 저장하고 temp랑 다음 원소가 같으면 원소 빼기
        # answer 배열을 만들어서 그 자리에 append()

def solution(arr):
    temp = -1
    answer = []
    for i in arr :
        if temp == i : continue
        else :
            answer.append(i)
            temp = i
    return answer