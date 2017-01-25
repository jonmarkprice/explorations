import unittest
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

    # Consider initiating content
    def test_unset(self):
        # Should raise NoValue if size of 1+
        with self.assertRaises(Bits.NoValue):
            Bits(1).array()

        # Should not raise NoValue for size of 0
        self.assertEqual(Bits(0).array(), [])
        self.assertEqual(Bits(0).num(), 0)

        with self.assertRaises(Bits.NoValue):
            Bits(1).num()

        
    def test_num(self):
        pass


if __name__ == '__main__':
    unittest.main()
