# phone_number의 자릿수에 맞춰 * 추가하기

def solution(phone_number):
    answer = []
    for i in phone_number[:-4] :
        answer.append('*')
    for j in phone_number[-4:] :
        answer.append(j)
    return ''.join(answer)