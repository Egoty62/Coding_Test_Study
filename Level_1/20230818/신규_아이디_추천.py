# 아이디의 길이는 3자 ~ 15자
# 알파벳 소문자, 숫자, -, _, . 만 사용가능
    # . 은 처음과 끝에 사용 못 하고, 연속으로 사용 못 함

# 1. 대문자를 소문자로
# 2. 허용되는 문자 외의 문자는 전부 삭제
# 3. 연속되는 마침표를 하나의 마침표로 대체
# 4. 처음 or 끝의 마침표 제거
# 5. 빈 문자열이라면 'a' 추가
# 6. 16자 이상일 경우, 뒤의 문자 삭제
    # 만약 삭제 후 마지막 문자가 마침표라면, 마침표도 삭제
# 7. 2자 이하의 경우, 마지막 문자를 길이가 3이 될 때 까지 반복해서 추가

import re

def solution(new_id):
    level1 = new_id.lower()
    
    level2 = ''.join(re.findall("[a-z0-9\-\.\_]", level1))
    
    level3 = ''
    continuous = 0
    for i in level2 :
        if i == '.' :
            if continuous != 0 :
                continue
            level3 += i
            continuous += 1
        else :
            level3 += i
            continuous = 0
    
    level4 = level3.strip('.')
    
    level5 = level4
    if len(level5) == 0 :
        level5 += 'a'
    
    level6 = level5[:15].rstrip('.')
    
    level7 = level6
    while len(level7) < 3 :
        level7 += level7[-1]
    
    return level7

# re.sub 도 활용 가능