# 딕셔너리 활용
# {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j'}

def solution(age):
    PROGRAMMER962 = {'0' : 'a', '1' : 'b', '2' : 'c', '3' : 'd', '4' : 'e', '5' : 'f', '6' : 'g', '7' : 'h', '8' : 'i', '9' : 'j'}
    return ''.join([PROGRAMMER962[i] for i in list(str(age))])
# list()를 굳이 넣지 않아도 됨

# 다른 사람의 풀이
def study(age):
    return ''.join([chr(int(i)+97) for i in str(age)])
# 유니코드 반환