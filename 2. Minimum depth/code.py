from collections import deque


def solve(root):
    res = []
    q = deque()
    cnt = 0 #/0 coz the first elem is also gonna append
    
    # 1 Initialise
    q.append(root)
    
    # 2. BFS with cndn
    while len(q):
        n = len(q)
        
        # 1. Cur lvl operations
        cnt += 1 
        
        for i in range(n):
            cur = q.popleft()
            
            # 1. Chk cndn
            if not root.left and not root.right: return cnt
            
            # 2. Add children
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)
    
    return cnt  #/ Cndn not matched {skew tree}