# arr1, arr2의 각 원소를 n자릿수의 이진수(문자열)로 변환
    # 나누기 2, 나머지가 있으면 1, 없으면 0
# 각 문자열을 비교 : 0이면 공백, 0이 아니면 #

def binary(n, arr) :
    bi_array = []
    for i in arr :
        bi_str = ''
        temp = i
        for j in range(n) :
            if temp % 2 == 0 : bi_str = bi_str + '0'
            else : bi_str = bi_str + '1'
            temp = temp // 2
        bi_array.append(bi_str)
    return bi_array
    
def mapping(n, a, b) :
    result_list = []
    space = ' '
    for i in range(n) :
        result_str = ''
        for j in range(n) :
            if a[i][j] == '0' and b[i][j] == '0' :
                result_str = space + result_str
            else : result_str = '#' + result_str
        result_list.append(result_str)
    return result_list
            
def solution(n, arr1, arr2):
    a = binary(n, arr1)
    b = binary(n, arr2)
    answer = mapping(n, a, b)
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i in range(n) :
        a = (bin(arr1[i] | arr2[i]))[2:]
        while len(a) < n :
            a = '0' + a
        a = a.replace('0', ' ')
        a = a.replace('1', '#')
        answer.append(a)
    return answer