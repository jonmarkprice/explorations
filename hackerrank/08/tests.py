import unittest
import random
from heap import Heap, median

class TestHeapSort(unittest.TestCase):
    
    def test_empty_insert(self):
        heap = Heap()
        heap.add(3)
        self.assertEqual(heap.pop(), 3)
        
    def test_empty_insert_2(self):
        heap = Heap()
        heap.add(3)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), None)
    
    def test_insert(self):
        #for i in range(50):
        n = 10
        heap = Heap()
        values = list(range(n))
        random.shuffle(values)
        for value in values:
            print('Inserting ' + str(value))
            heap.add(value)
            print(heap.array)

        # TODO: write a test to examine heap property
        tmp = Heap(heap.array[:])
        print('Original: ' + str(tmp.array))
        tmp.heapify()
        print('Heapified: ' + str(tmp.array))
        for i in range(n):
            print('Expecting ' + str(i))
            print('Before: ' + str(tmp.array))
            self.assertEqual(tmp.pop(), i)
            print('After:  ' + str(tmp.array))
            #heap.sort()
            #self.assertTrue(median(heap.array), median(sorted(values)))
        
if __name__ == '__main__':
    unittest.main()
