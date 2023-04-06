def solution(i, j, k):
    answer = 0
    list_ij_int = [x for x in range(i, j + 1)]
    list_ij_str = ''.join([i for i in str(list_ij_int)])
    
    return list_ij_str.count(str(k))