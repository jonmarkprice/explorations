#from math import log, floor
import math

''' 
Extra credit: Enforce balance
'''
class node:
    def __init__(self, data):
        # Constraints:
        # data is not None
        # data >= 0
        # data <= 10000
        
        self.data = data
        self.left = None
        self.right = None

class node():
    def __init__(self, data):
        # Constraints:
        # data is not None
        # data >= 0
        # data <= 10000
        
        self.data = data
        self.left = None
        self.right = None

def check_bst(root, verbose=False):
    LLIM = -1
    RLIM = 10001
    status, count, level = recur(root, LLIM, RLIM, 0, 1, verbose)
    
    if verbose:
        print('level {}, count {}, status {}'.format(level, count, status))
    if level > math.floor(math.log(count, 2)):
        status = False
        if verbose:
            print("Didn't pass!")
    
    return status

# Working
def recur(root, llim, rlim, level, count, verbose=False):
    if root is None:
        return (True, None)
    
    status      = True
    left_count  = count
    right_count = count
    left_level  = level
    right_level = level
    
    if root.left is not None:
        if root.left.data < root.data and root.left.data > llim:
            status, left_count, left_level = recur(root.left, llim, root.data, level + 1, count + 1, verbose)
            if verbose and status is False:
                print('left ' + str(status))
        else:
            status = False

    if status is True:
        #return (False, None)
        right_count = left_count
        if root.right is not None:
            if root.right.data > root.data and root.right.data < rlim:
                status, right_count, right_level = recur(root.right, root.data, rlim, level + 1, left_count + 1, verbose)
                if verbose and status is False:
                    print('right ' + str(status))
            else:
                status = False
                #return (False, None)

    return (status, right_count, max(right_level, left_level))
    
# XXX:
# do I need to check for an unbalanced (degenerate) tree?
# let's assume yes:
'''
            a
        b       c
    d      e f      g
    
levels:     nodes:
1           [1]
2           [2, 3]
3           [4, 6]

1 + 2 + 4 + 8 + ...



'''
'''
        * (0, 1)
      * (1, 2)  - (,
    * (2, 3)  - (2, x)   -
 -      * (3, 4)
 
log(1, _) -> 0
level = 0 
0 > 0 --> false, OK
log(2, 2) -> 1

level (2) 
2 > 2 -- not true, Ok

        *
    -       * (N 2 , L 1)
                * (N3, L2)
1 <= log(2)
3 <= ceil(log(3)) 2


'''
