def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)) :
        for j in range(len(arr1[0])) :
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

def solution2(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer