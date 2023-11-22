# 모든 노드는 서로 다른 x 값을 가진다
# 같은 레벨에 있는 노드는 같은 y 좌표를 가진다
# 임의의 노드 V의 왼쪽 서브트리에 있는 노드의 x값은 V.x 보다 항상 작다
# 임의의 노드 V의 오른쪽 서브트리에 있는 노드의 x값은 V.x 보다 항상 크다 
# 잘못 된 정수 좌표는 없다

# DFS 구현 with 스택
    # node의 가장 첫 원소를 스택에 추가
    # while stack
        # stack의 마지막 원소 저장
        # 

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