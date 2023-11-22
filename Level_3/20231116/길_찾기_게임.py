import sys
sys.setrecursionlimit(10 ** 6)

def solution(nodeinfo):
    if len(nodeinfo) == 1 : return [[1], [1]]

    axis = {str(j) : (nodeinfo.index(j) + 1) for j in nodeinfo}
    node = max(nodeinfo, key= lambda x : x[1])
    level = sorted(list(set([k[1] for k in nodeinfo])), reverse= True)
    nodedict = {l : sorted([j for j in nodeinfo if j[1] == l]) for l in level}
    
    def maketree(plist, s : int, e : int) :
        a, b = plist
        if level[level.index(b)] != level[-1] :
            nodelist = [k for k in nodedict[level[level.index(b) + 1]] if k[0] > s and k[0] < e]
            for i in nodelist :
                if i[0] < a :
                    preorder.append(axis[str(i)])
                    maketree(i, s, a)
                    postorder.append(axis[str(i)])
                elif i[0] > a :
                    preorder.append(axis[str(i)])
                    maketree(i, a, e)
                    postorder.append(axis[str(i)])

        return
        
    
    preorder = [axis[str(node)]]
    postorder = []
    maketree(node, -1, 100001)
    postorder.append(axis[str(node)])

    return [preorder, postorder]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

# https://school.programmers.co.kr/learn/courses/30/lessons/42892