def solution(players, callings):
    players_dict = {k : v for k, v in enumerate(players)} # {0 : 'mumu'}
    rev_dict = {v : k for k, v in players_dict.items()}   # {'mumu' : 0}

    for i in callings :
        idx = rev_dict[i]
        temp = players_dict[idx - 1]
        players_dict[idx - 1] = i
        players_dict[idx] = temp
        rev_dict[i] -= 1
        rev_dict[temp] += 1
        
    return [players_dict[i] for i in range(len(players))]