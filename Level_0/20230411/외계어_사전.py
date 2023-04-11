# spell의 알파벳을 한 번씩만 써서 dic에 존재하는 단어를 만들어야 함
    # spell의 크기와 dic 단어의 길이가 같음
    # count를 했을 때 spell과 dic의 단어가 같은 값이 나옴
        # 이중 반복문
            # spell과 길이가 같은 것들을 고름
                # 고른 단어 중에서 count가 같은게 있으면 1, 없으면 2

def solution(spell, dic):
    a = []
    for i in dic :
        if len(list(i)) == len(spell) :
            a.append(i)
    
    for j in a :
        temp = 0
        for k in spell :
            if spell.count(k) == j.count(k) :
                temp += 1
            else : break
            
            if temp == len(spell) :
                return 1
        
    return 2

# 다른사람의 풀이 : set 활용
    # 내 추가적인 생각 : len이 같을 때, 두 set의 합집합이 처음 set와 같을 경우 return 1

# 제한사항에 중복된 원소를 갖지 않는다는 조건을 고려하지 못 함