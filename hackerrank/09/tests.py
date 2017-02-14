import unittest
from partial import PartialTrie

class TestKeyTrie(unittest.TestCase):
 
    def test_hr_01(self):
        p = PartialTrie()
        p.add('hack')
        p.add('hackerrank')
        p.print_trie()
        self.assertEqual(p.count('hac', True), 2)
        self.assertEqual(p.count('hak', True), 0)
 
    def test_backwards(self):
        p = PartialTrie()
        p.add('abc')
        p.add('a')
        self.assertEqual(p.find('ab'), ['abc'])
        self.assertEqual(p.find('a'), ['a', 'abc'])
 
    def test_add_multiple(self):
        p = PartialTrie()
        p.add('a')
        p.add('b')
        p.add('ab')
        
        self.assertTrue(p.find('a'), ['a', 'ab'])
        self.assertTrue(p.find('b'), ['b'])
        self.assertTrue(p.find('ab'), ['ab'])
    '''
    # USE non-public api
    #k.head.nodes[0]
    def test_find_nonapi(self):
        k = KeyTrie()
        k.head.nodes[0] = Node(1)
        self.assertEqual(k.find('a'), 1)
    '''
    
    def test_not_found(self):
        p = PartialTrie()
        p.add('b')
        self.assertEqual(p.find('a'), [])

    @unittest.skip('')
    def test_partial(self):
        k = KeyTrie()
        k.addNode('hack', Node(0))
        k.addNode('hackerrank', Node(0))
        
        print(k.find('hac'))
        print(k.find('hak'))
        #self.assertTrue(k.find('hac'), 0) #
        #self.assartFalse(k.find('hak'), 1)
        
        # TODO  NEED FIND PARTIAL FUNCTION
if __name__ == '__main__':
    unittest.main()
