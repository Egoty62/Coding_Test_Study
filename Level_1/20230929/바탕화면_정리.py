def solution(wallpaper):
    answer = []
    
    for i in range(len(wallpaper)) :
        if '#' in wallpaper[i] :
            answer.append(i)
            break
    
    answer.append(min([i.find('#') for i in wallpaper if i.find('#') != -1]))
    
    for i in range(len(wallpaper) - 1, -1, -1) :
        if '#' in wallpaper[i] :
            answer.append(i + 1)
            break
            
    answer.append(max([i.rfind('#') for i in wallpaper]) + 1)
            
    return answer