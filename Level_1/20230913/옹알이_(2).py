def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    babbling_dup_x = []
    temp_list = []
    
    for i in babbling :
        dup = False
        for j in word :
            if j * 2 in i :
                dup = True
            else : continue
        if dup == False :
            babbling_dup_x.append(i)
            
    print(babbling_dup_x)
    
    for i in babbling_dup_x :
        temp_word = i
        for j in word :
            if j in i :
                temp_word = temp_word.replace(j, '0')
        temp_list.append(temp_word)        
    
    result = 0
    
    for i in temp_list :
        if i.isdigit() :
            result += 1

    return result