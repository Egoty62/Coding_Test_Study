def solution(participant, completion):
    dict_part = {}
    answer = 0
    for i in participant :
        dict_part[hash(i)] = i
        answer += hash(i)
    for j in completion :
        answer -= hash(j)
    return dict_part[answer]

# counter를 사용해서 풀 수도 있음(해시보다 시간은 좀 더 걸림)
    # counter는 빼기가 가능함