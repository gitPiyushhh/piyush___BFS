from collections import deque


def solve(root, x, y):
    #/ Edge case
    if not root: return False
    
    q = deque()
    flag = False
    
    # 1. Intitalistion
    q.append(root)
    
    # 2. BFS{with cndn}
    while len(q):
        n = len(q)
        lvl = []
        
        for i in range(n):
            cur = q.popleft()
            
            # 1. Cur lvl
            lvl.append(cur.val)
            
            # 2. Children append{with cndn chck}
            if cur.left and cur.right:
                if (cur.left.val == x and cur.right.val == y) or (cur.left.val == y and cur.right.val == x):
                    flag = False
            
            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
        
        #/ Onc complete lvl prepared till here
        # 2. Present
        if x in lvl and y in lvl and not flag:
            return True
        
    #3. Not presend
    return False