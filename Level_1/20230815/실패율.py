def solution(N, stages):
    fail_per = {}
    player = len(stages)
    
    for i in range(1, N + 1) :
        if player <= 0 :
            fail_per[i] = 0
        else :
            fail_per[i] = stages.count(i) / player
            player -= stages.count(i)
            
    return [i[0] for i in sorted(fail_per.items(), key= lambda x : -x[1])]