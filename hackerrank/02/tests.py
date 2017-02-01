import unittest
from soln import number_needed

class AnagramCreation(unittest.TestCase):
    # no setup or teardown
    
    def test_simple(self):
        a = 'bak'
        b = 'zkca'
        self.assertEqual(3, number_needed(a, b))
        
    def test_empty(self):
        a = ''
        b = 'aceuaoeudoth'
        self.assertEqual(len(b), number_needed(a, b))
    
    def test_both_empty(self):
        self.assertEqual(0, number_needed('', ''))
    
    def test_both_equal(self):
        a = 'aoeuhtoa'
        self.assertEqual(0, number_needed(a, a))

if __name__ == '__main__':
    unittest.main()
