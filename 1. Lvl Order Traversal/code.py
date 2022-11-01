import copy


def solve(root):
    #/ Base cases
    if not root: return []
    
    res = []
    que = []
    
    # 1. Initialise
    
    while len(que):
        lvl = []
        n = len(que)
        
        # 2. Inner loop
        for i in range(n):
            # (a) Cur
            cur = que.pop()
        
            # (b) Res append
            lvl.append(cur.val)
        
            # (c) Children
            if cur.left: que.append(cur.left)
            if cur.right: que.append(cur.right)            
        

    # 3. Move lvl
    lvl1 = copy.deepcopy(lvl)
    res.append(lvl1)
    
    return res

