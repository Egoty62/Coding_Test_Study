def solution(n, t, m, timetable):
    timetable.sort()
    idx = 0
    time = "09:00"
    lensize = len(timetable)

    def addtime(str_, num_) :
        str_ = [int(i) for i in str_.split(":")]
        str_[1] += num_
        if str_[1] >= 60 :
            str_[1] -= 60
            str_[0] += 1
        elif str_[1] < 0 :
            str_[1] += 60
            str_[0] -= 1
        str_ = [str(i) for i in str_]
        for i in range(len(str_)) :
            if len(str_[i]) == 1 :
                str_[i] = "0" + str_[i]
        return ":".join([i for i in str_])
    
    time = addtime(time, -t)

    for _ in range(n) :
        time = addtime(time, t)
        if idx >= lensize : continue
        if _ == n - 1 :
            last = 0
            for i in range(m) :
                if idx >= lensize : pass
                elif timetable[idx] <= time :
                    idx += 1
                    last += 1
                if i == m - 1 :
                    if last < m :
                        return time
                    else :
                        return addtime(timetable[idx - 1], -1)
        else :
            for _ in range(m) :
                if timetable[idx] <= time :
                    idx += 1
        
    return time

# https://school.programmers.co.kr/learn/courses/30/lessons/17678