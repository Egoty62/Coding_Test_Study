def solution(record):
    answer = []
    record = [i.split() for i in record]
    id = {i[1] : i[2] for i in record if i[0] != "Leave"}

    leave = "님이 나갔습니다."
    enter = "님이 들어왔습니다."

    for i in record :
        if i[0] == "Enter" :
            answer.append(id[i[1]] + enter)
        elif i[0] == "Leave" :
            answer.append(id[i[1]] + leave)
    
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42888