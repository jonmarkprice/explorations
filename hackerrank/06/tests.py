import unittest
from soln import MyQueue

class QueueTest(unittest.TestCase):

    def test_single_enqueue(self):
        q = MyQueue()
        q.put(5)
        self.assertEqual(5, q.peek())
        
    def test_double_enqueue(self):
        q = MyQueue()
        q.put(3)
        q.put(4)
        self.assertEqual(3, q.peek())
        
    def test_empty_stack(self):
        q = MyQueue()
        q.peek()
    
    def test_double_enqueue_pop(self):
        q = MyQueue()
        q.put(3)
        q.put(4)
        self.assertEqual(3, q.pop())
        q.put(5)
        self.assertEqual(4, q.pop())

    def test_print(self):
        q = MyQueue()
        q.put(43)
        self.assertEqual(43, q.peek())
        q.put(41)
        self.assertEqual(43, q.pop())
        self.assertEqual(41, q.pop())
        self.assertEqual(None, q.peek())
        for i in range(10):
            q.put(i)
        for i in range(10):
            self.assertEqual(q.pop(), i)
            

    def test_random(self):
        q = MyQueue()
        q.pop()
        q.put(4)
        q.peek()
        q.put(4)
        q.put(6)
        q.pop()
        q.pop()
        q.put(4)
        q.put(23)
        q.put(6)
        q.pop()
        q.peek()
        q.put(32)
        q.pop()
        q.pop()
        q.pop()
        q.pop()

if __name__ == '__main__':
    unittest.main()
