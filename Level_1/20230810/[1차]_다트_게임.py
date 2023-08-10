# 문자열을 split()으로 리스트로 나누기
# 리스트에 임시로 점수를 저장하고 한 번에 계산하기

def solution(dartResult):
    list_dart = []
    str_dart = ''
    for i in dartResult :
        if i.isdigit() :
            str_dart = str_dart + i
        else :
            if str_dart.isdigit() :
                list_dart.append(int(str_dart))
                str_dart = ''
            
            if i == 'D' :
                list_dart[-1] = list_dart[-1] ** 2
            elif i == 'T' :
                list_dart[-1] = list_dart[-1] ** 3
            elif i == '*' :
                list_dart[-1] *= 2
                if len(list_dart) >= 2 :
                    list_dart[-2] *= 2
                else : continue
            elif i == '#' :
                list_dart[-1] *= -1
            
    answer = sum(list_dart)
    return answer

# import re를 활용한 정규표현식 또는 딕셔너리를 사용하여 해결도 가능함