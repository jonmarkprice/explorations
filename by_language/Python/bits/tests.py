import unittest
import bits
from bits import Bits

class BitTests(unittest.TestCase):
    def test_len(self):
        self.assertEqual(len(Bits(0)), 0)
        self.assertEqual(len(Bits(5)), 5)

    def test_set(self):
        a = Bits(3)
        a.set([0, 0, 0])

        self.assertEqual(a.array(), [0, 0, 0])

    def test_clear(self):
        a = Bits(3)
        a.clear()
        self.assertEqual(a.array(), [0, 0, 0])

        # TODO: an set() of the wrong size should raise an exception
        with self.assertRaises(bits.BadSet): # XXX better name?
            a.set([0])
        with self.assertRaises(bits.BadSet):    # different for underflow
            a.set([0, 0, 0, 0])                 # and overflow?

    # Consider initiating content
    def test_unset(self):
        # Should raise NoValue if size of 1+
        with self.assertRaises(bits.NoValue):
            Bits(1).array()

        # Should not raise NoValue for size of 0
        self.assertEqual(Bits(0).array(), [])
        self.assertEqual(Bits(0).num(), 0)

        with self.assertRaises(bits.NoValue):
            Bits(1).num()
        
    def test_num(self):
        a = Bits(3)
        a.set([1, 1, 0])
        self.assertEqual(a.num(), 6)

    def test_slice(self):
        # I want a way to be able to get a slice of bits and set
        # them, which should update the whole object.
        a = Bits(5)
        a.clear()
        b = a.slice(0, 3) # inclusive (first 4 bits)
        b.set([0, 1, 1, 0])
        self.assertEqual(a.array(), [0, 1, 1, 0, 0])

if __name__ == '__main__':
    unittest.main()
