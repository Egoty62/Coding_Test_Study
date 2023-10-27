def change_2(a, b, arr) :
    if a == 1 :
        count0, count1 = 0, 0
        for i in range(b) :
            count0 += sum([1 for num in arr[i] if num == 0])
            count1 += sum([1 for num in arr[i] if num == 1])
        
        answer.append(count0)
        answer.append(count1)
        return
    else :
        zip_bull = True
        for i in range(0, b, a) :
            for j in range(0, b, a) :
                temp = arr[i][j]
                for k in range(i, i + a) :
                    for l in range(j, j + a) :
                        if arr[k][l] != temp or arr[k][l] == 2 :
                            zip_bull = False
                            break
                if zip_bull :
                    for m in range(i, i + a) :
                        for n in range(j, j + a) :
                            if m == i and n == j : continue
                            else : arr[m][n] = 2
                zip_bull = True
        a = a // 2

    change_2(a, b, arr)

def solution(arr):
    global answer
    answer = []
    b = len(arr)
    change_2(b, b, arr)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/68936