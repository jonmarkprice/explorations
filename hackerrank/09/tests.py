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
        self.assertEqual(p.count('ab'), 1)
        self.assertEqual(p.find('a'), ['a', 'abc'])
        self.assertEqual(p.count('a'), 2)
 
    def test_add_multiple(self):
        p = PartialTrie()
        p.add('a')
        p.add('b')
        p.add('ab')
        
        self.assertEqual(p.find('a'), ['a', 'ab'])
        self.assertEqual(p.find('b'), ['b'])
        self.assertEqual(p.find('ab'), ['ab'])
        self.assertEqual(p.count('a'), 2)
        self.assertEqual(p.count('b'), 1)
        self.assertEqual(p.count('ab'), 1)

    def test_not_found(self):
        p = PartialTrie()
        p.add('b')
        self.assertEqual(p.find('a'), [])

    def test_empty_key(self):
        p = PartialTrie()
        p.add('')
        p.find('')
        self.assertEqual(p.count(''), 0)

    def test_key_single_key(self):
        p = PartialTrie()
        p.add('a')
        self.assertEqual(p.find('a'), ['a'])
        self.assertEqual(p.count('a'), 1)
        self.assertEqual(p.find('b'), [])
        self.assertEqual(p.count('b'), 0)

if __name__ == '__main__':
    unittest.main()
