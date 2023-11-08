def solution(info, edges):
    n = len(info)
    sheeplist = []
    visited = {i : False for i in range(n)}
    info = {i : j for i, j in zip(range(n), info)}

    visited[0] = True

    def sheepwolf(sheep_, wolf_) :
        if sheep_ > wolf_ : sheeplist.append(sheep_)
        else :  
            return
        
        for a, b in edges :
            if visited[a] == True and visited[b] == False :
                visited[b] = True
                if info[b] == 0 :
                    sheepwolf(sheep_ + 1, wolf_)
                    sheeplist.append(sheep_)
                else : sheepwolf(sheep_, wolf_ + 1)
                visited[b] = False

            
    sheepwolf(1, 0)

    return max(sheeplist)

# https://school.programmers.co.kr/learn/courses/30/lessons/92343