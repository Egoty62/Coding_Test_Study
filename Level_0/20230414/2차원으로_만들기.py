# 리스트 컴프리헨션 사용
# num_list에서 n개씩 분할해서 2차원 리스트로 다시 만듦
# 첫 번째 차원은 0 ~ len(num_list) // n까지 있음 (range 사용 기준)
    # 두 번째 차원은 0 ~ n까지 있음 (range 사용 기준)


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = 2

def practice(num_list : list, n : int) :
    answer = [[], [], [], []]
    i = 0
    for j in num_list :
        answer[i].append(j)
        if len(answer[i]) >= n : i += 1

    return answer

# 대충 위와 같은 코드가 나옴
    # answer의 크기를 올바르게 설정해야 코드가 제대로 동작함

# 리스트 컴프리헨션
def solution(num_list, n):
    return [[i for i in num_list[j * n : (j + 1) * n]] for j in range(len(num_list) // n)]