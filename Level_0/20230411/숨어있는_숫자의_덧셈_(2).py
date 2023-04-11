# my_string에서 영어는 공백으로 바꾸고, 숫자는 그대로
    # 그대로 리스트화, 공백을 포함한 문자열로 다시 만듦
        # 그 후 공백을 삭제한 리스트로 다시 만듦(연속된 숫자가 있을 경우 하나의 수로 표기하기 위해)
            # 리스트 안의 문자열을 정수로 바꾼 후 sum()

# import re 후 정규표현식을 사용하여 풀기도 가능
    # re.findall로 수만 다 찾고, 그것을 정수로 만들어 sum()

def solution(my_string):
    answer = []
    for i in my_string :
        if i.isalpha() :
            answer.append(" ")
        else : answer.append(i)
    
    a = "".join(answer)
    
    return sum([int(i) for i in a.split()])

def solution2(my_string) :
    import re
    return sum([int(i) for i in re.findall(r"[0-9]+", my_string)])