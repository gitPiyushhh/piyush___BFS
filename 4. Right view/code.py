from collections import deque


def solve(root):
    #/ Edge case
    if not root: return []
    
    # 1. Intitalistion
    q = deque([root])
    res = []
    
    # 2. BFS{with cndn}
    while len(q):
        n = len(q)
        
        # 1. Cur lvl
        for i in range(n):
            cur = q.popleft()
            
            # 1. Cndn: Right view{last elem}
            if i == len(q) - 1: res.append(cur)
            
            # 2. Children append 
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
    
    return res
    
