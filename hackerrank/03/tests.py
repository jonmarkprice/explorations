import unittest
from soln import ransom_note

class RansomeNote(unittest.TestCase):
    # no setup or teardown
    
    def test_simple(self):
        mag = 'hello world how are you'
        rn  = 'hello world'
        self.assertTrue(ransom_note(mag, rn))
    
    def test_not_possible(self):
        mag = 'hi world how are you'
        rn  = 'hello world'
        self.assertFalse(ransom_note(mag, rn))

    def test_theirs(self):
        mag = 'give me one grand today night'
        rn  = 'give one grand today'
        self.assertTrue(ransom_note(mag, rn))

if __name__ == '__main__':
    unittest.main()
