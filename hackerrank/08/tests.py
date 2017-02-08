import unittest
from soln import Heap

class TestHeapSort(unittest.TestCase):
    
    def test_empty_insert(self):
        heap = Heap()
        heap.insert(3)
        self.assertEqual(heap.pop(), 3)
        
    def test_empty_insert_2(self):
        heap = Heap()
        heap.insert(3)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), None)
    '''
    def test_insert(self):
        heap = Heap()
        # TODO Shuffle
        values = list(range(10))
        for value in values:
            print('Inserting ' + str(value))
            heap.insert(value)
        
        for value in values:
            print('Trying ' + str(value))
            self.assertEqual(heap.pop(), value)
            #print(' ... OK!', end='')
    '''
if __name__ == '__main__':
    unittest.main()
