def solution(cards1, cards2, goal):
    for i in goal :
        try :
            if cards1[0] == i :
                cards1.remove(i)
            else :
                try :
                    if cards2[0] == i :
                        cards2.remove(i)
                    else : return 'No'
                except IndexError :
                    return 'No'
        except IndexError :
            try :
                if cards2[0] == i :
                    cards2.remove(i)
                else : return 'No'
            except IndexError :
                return 'No'
    return 'Yes'