# split()으로 단어를 나눠줌 => X
# 문자열 s의 맨 앞과 맨 뒤에 공백이 있을 경우도 고려
# 하나 이상의 공백문자
    # split() 사용하면 안 될것 같음


# 아스키 코드 활용
    # 아스키 코드 말고 lower(), upper() 사용하기

def solution(s):
    answer = ''
    index = 0
    for i in s :
        if i == ' ' :
            index = 0
            answer += i
        else :
            if index % 2 == 0 :
                answer += i.upper()
            elif index % 2 != 0 :
                answer += i.lower()
            index += 1
    return answer