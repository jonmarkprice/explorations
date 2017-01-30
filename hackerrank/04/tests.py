import unittest
from soln import has_cycle, Node

class DetectCycle(unittest.TestCase):
    # no setup or teardown
    
    def test_null_list(self):
        head = None
        self.assertFalse(has_cycle(head))

    def test_simple_list(self):
        head = Node(None, None)
        self.assertFalse(has_cycle(head))

    def test_short_cycle(self):
        a, b = Node(), Node()
        a.next = b
        b.next = a
        self.assertTrue(has_cycle(a))
        
    def test_cycle(self):
        a, b, c = [Node()] * 3
        a.next = b
        b.next = c
        c.next = None
        self.assertFalse(has_cycle(a))
        
if __name__ == '__main__':
    unittest.main()
