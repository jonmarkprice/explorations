class node():
    def __init__(self, data):
        # Constraints:
        # data is not None
        # data >= 0
        # data <= 10000
        
        self.data = data
        self.left = None
        self.right = None

# global constraints
LLIM = -1
RLIM = 10001

def check_binary_search_tree_(root, llim=LLIM, rlim=RLIM):
    if root is None:
        return True
    
    if root.left is not None:
        if root.left.data < root.data and root.left.data > llim:
            status = check_binary_search_tree_(root.left, llim, root.data)
            if status is False:
                return False
        else:
            return False
            
    if root.right is not None:
        if root.right.data > root.data and root.right.data < rlim:
            status = check_binary_search_tree_(root.right, root.data, rlim)
            if status is False:
                return False
        else:
            return False

    return True
