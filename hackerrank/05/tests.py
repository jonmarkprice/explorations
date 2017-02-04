import unittest
from soln import is_matched

class MatchBrackets(unittest.TestCase):
    # no setup or teardown
    def test_simple_parens(self):
        self.assertTrue(is_matched('()'))
        
    def test_mingled(self):
        self.assertFalse(is_matched('([)]'))
    
    def test_nested_unmatched(self):
        self.assertFalse(is_matched('{[(})]}'))
        
    def test_bad_input(self):
        self.assertFalse(is_matched('(a)'))

if __name__ == '__main__':
    unittest.main()
