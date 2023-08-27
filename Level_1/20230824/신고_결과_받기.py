def solution(id_list, report, k):
    answer = []
    tuplist = list(set([tuple(i.split()) for i in report]))
    maillist = {i : 0 for i in id_list}
    reportlist = {i : 0 for i in id_list}
    
    for i in range(len(tuplist)) :
        reportlist[tuplist[i][1]] += 1
        
    for i in tuplist :
        if reportlist[i[1]] >= k :
            maillist[i[0]] += 1
    
    for i in id_list :
        answer.append(maillist[i])
        
    return answer