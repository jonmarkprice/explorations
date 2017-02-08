import unittest
from soln import Node, KeyTrie

class TestKeyTrie(unittest.TestCase):
 
    def test_add_multiple(self):
        k = KeyTrie()
        k.addNode('a', Node(42))
        k.addNode('b', Node(1))
        k.addNode('ab', Node(10))
        self.assertTrue(k.find('a'), 42)
        self.assertTrue(k.find('b'), 1)
        self.assertTrue(k.find('ab'), 10)
    
    # USE non-public api
    #k.head.nodes[0]
    def test_find_nonapi(self):
        k = KeyTrie()
        k.head.nodes[0] = Node(1)
        self.assertEqual(k.find('a'), 1)

    def test_find(self):
        k = KeyTrie()
        k.addNode('a', Node(1))
        self.assertEqual(k.find('a'), 1)
    
    def test_find_multiple_nonapi(self):
        k = KeyTrie()
        k.addNode('a', Node(3))
        k.addNode('b', Node(1))
        k.head.nodes[0].nodes[1] = Node(4)
        self.assertEqual(k.find('ab'), 4)

    def test_add_multiple(self):
        k = KeyTrie()
        k.addNode('a', Node(42))
        k.addNode('b', Node(1))
        k.addNode('ab', Node(10))
        self.assertTrue(k.find('a'), 42)
        self.assertTrue(k.find('b'), 1)
        self.assertTrue(k.find('ab'), 10)

if __name__ == '__main__':
    unittest.main()
