# sorted(), key = lambda x : x[n] 사용하기
    # x[n]이 같을 경우 두 번째 정렬 조건인 사전순 정렬을 위해 lambda x : (x[n], x) 사용

def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n], x))