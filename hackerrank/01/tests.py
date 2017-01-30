import unittest
import soln

class ArrayRotation(unittest.TestCase):
    # no setup or teardown

    def test_rot1_pair(self):
        self.assertEqual(soln.rot1([1, 2]), [2, 1])

    def test_rot1_array(self):
        self.assertEqual(soln.rot1([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_rot1_single(self):
        self.assertEqual(soln.rot1([1]), [1])
        self.assertEqual(soln.rot(1, [0]), [0])

    def test_rot_2_pair(self):
        # Rotating a pair twice returns itself
        self.assertEqual(soln.rot(2, [1, 2]), [1, 2])

    def test_rot(self):
        self.assertEqual(soln.rot(2, [1, 2, 3, 4, 5]), [3, 4, 5, 1, 2])

if __name__ == '__main__':
    unittest.main()
