import unittest
from soln import node
from soln import check_binary_search_tree_ as is_bst

class IsBST(unittest.TestCase):
    # no setup or teardown
    
    # def test_null_data(self)
    def test_single_root(self):
        tree = node(0)
        self.assertTrue(is_bst(tree))
    
    def test_left(self):
        root = node(1)
        left = node(0)
        root.left = left
        self.assertTrue(is_bst(root))
        
    def test_right(self):
        root = node(0)
        right = node(1)
        root.right = right
        self.assertTrue(is_bst(root))
        
    def test_left_larger(self):
        root = node(0)
        left = node(1)
        root.left = left
        self.assertFalse(is_bst(root))

    def test_unbalanced_tree(self):
        root    = node(0)
        right1  = node(1)
        right2  = node(2)
        root.right = right1
        right1.right = right2
        
        # XXX assuming we don't care if the tree is balanced
        self.assertTrue(is_bst(root))

    def test_small_bst(self):
        left, right = [None], [None]
        root        = node(100)
        left[0]     = node(5)
        right[0]    = node(1242)
        root.left   = left[0]
        root.right  = right[0]
        
        self.assertTrue(is_bst(root))
    
    def test_small_bad_bst(self):
        left, right = [None], [None]
        root        = node(1)
        left[0]     = node(5)
        right[0]    = node(1242)
        root.left   = left[0]
        root.right  = right[0]
        
        self.assertFalse(is_bst(root))

    # FULL
    # Copy without list stuff...
    def test_big_bst(self):
            #depth       = 2
            #left = [None] * depth
            #right = [None] * depth
            root      = node(100)
            left0     = node(5)
            right0    = node(1242)
            
            left0.left = node(1)
            left0.right = node(6)
            
            right0.left = node(106)
            right0.right = node(1300)
            
            root.left   = left0
            root.right  = right0

            self.assertTrue(is_bst(root))
            
    def test_big_bad_bst(self):
            #depth       = 2
            #left = [None] * depth
            #right = [None] * depth
            root      = node(100)
            left0     = node(5)
            right0    = node(1242)
            
            left0.left = node(1)
            left0.right = node(6)
            
            right0.left = node(106)
            right0.right = node(1000) # < 1242
            
            root.left   = left0
            root.right  = right0

            #print('=============')
            self.assertFalse(is_bst(root))
            #print('=============')

    def test_repeated(self):
        root = node(3)
        left = node(3)
        right = node(4)
        root.left = left
        root.right = right
        self.assertFalse(is_bst(root))
        
    # TODO: test non-full
    def test_small_non_full(self):
        root = node(1)
        left = node(0)
        root.left = left
        self.assertTrue(is_bst(root))        
        #       1
        #   0       -

    def test_left_right_greater_than_root(self):
        root      = node(100)
        left0     = node(5)
        right0    = node(1242)
        
        left0.left = node(1)
        left0.right = node(101)
        
        right0.left = node(106)
        right0.right = node(1300)
        
        root.left   = left0
        root.right  = right0

        #print('=============')
        self.assertFalse(is_bst(root))
        #print('=============')
        
if __name__ == '__main__':
    unittest.main()
