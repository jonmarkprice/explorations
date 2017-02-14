import unittest
from partial import PartialTrie

class TestKeyTrie(unittest.TestCase):

    def test_hr_01(self):
        p = PartialTrie()
        p.add('hack')
        p.add('hackerrank')
        self.assertEqual(p.count('hac'), 2)
        self.assertEqual(p.count('hak'), 0)
 
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

    def test_empty_key(self):
        p = PartialTrie()
        p.add('')
        p.find('')

    def test_key_single_key(self):
        p = PartialTrie()
        p.add('')
        p.find('')
        
if __name__ == '__main__':
    unittest.main()
