# 윤년이므로 2월 29일까지 계산해야함
# 1, 3, 5, 7, 8, 10, 12월은 31일까지
# 4, 6, 9, 11월은 30일까지
# 2월은 29일까지
# 막무가내로 처리하기
# 1 ~ 12월을 리스트로 다 만듦
    # 2차원 딕셔너리 만들기

def solution(a, b):
    month_day_dict = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    month_list = [i for i in range(1, 13) for j in range(month_day_dict[i])]
    day_list = [[j + 1 for j in range(month_day_dict[i])] for i in range(1, 13)]
    dow_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE' , 'WED', 'THU'] * 53
    answer_list = [dow_list[0:31], dow_list[31:60], dow_list[60:91], dow_list[91:121], dow_list[121:152], dow_list[152:182], dow_list[182:213], dow_list[213:244], dow_list[244:274], dow_list[274:305], dow_list[305:335], dow_list[335:366]]

    answer_dict = {i + 1 : {day : dow for day, dow in zip(day_list[i], answer_list[i])} for i in range(12)}
    return answer_dict[a][b]