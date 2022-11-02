from collections import deque
import copy


def solve(root):
    #/ Edge cases
    if not root: return []
    
    res = []
    q = deque()
    leftToRight = True  #/ First lvl is left to right
    
    # 1. Initialise
    q.append(root)
    
    # 2. BFS with cndn 
    while len(q):
        n = len(q)
        lvl = []
        
        # 1. Create cur lvl
        for i in range(n):
            cur = q.popleft()
            lvl.append(cur.val)
        
        # 2. Chck cndn
        if not leftToRight:
            lvl1 = copy.deepcopy(lvl)
            res.append(lvl[::-1])   #/ Reverse for this case
        
        if leftToRight:
            lvl1 = copy.deepcopy(lvl)
            res.append(lvl)   #/ Reverse for this case
        
        # 3. Toggle flag
        leftToRight = not leftToRight
    
    return res