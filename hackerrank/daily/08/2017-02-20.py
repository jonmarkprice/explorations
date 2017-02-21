#!/bin/python3

class Heap():
    def __init__(self):
        self.array = []
        self.copy  = []
    
    def add(self, i):
        self.array.append(i)

    def median(self):
        # min heap
        
        # create copy
        #copy = array[:]
        
        # to find median
        # 1 create ordered array (heap sort)
        copy = self.heapsort(self.array[:])
        
        # 2 find median
        if len(copy) == 0:
            return None

        if len(copy) % 2 == 0: # even
            a = [len(copy) // 2 - 1]
            b = copy[len(copy) // 2]
            return (a + b) / 2.0
            
        else: # odd
            return float(copy[len(copy) // 2])
            

    def reheap(self, index = 0):
        '''Preserve our heap property'''
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        # children less (or eq) than parent
        
        # what if not defined
        if len(self.array) > left_index:
            if self.array[index] > self.array[left_index] or self.array[index] is None:
                # >= property is transitive so no need to rescan
                # swap head and index
                self.array[index], self.array[left_index] = self.array[left_index], self.array[index]
            # recur
            self.reheap(left_index)

            if len(self.array) > right_index:
                if self.array[index] > self.array[right_index] or self.array[index] is None:
                    #swap
                    self.array[index], self.array[right_index] = self.array[right_index], self.array[index]
                self.reheap(right_index)

    # This is not even colse to done...
    def heapsort(self, arr, index = 0):
        if arr[index] is not None:
            arr.append(index)
            self.reheap(index)
        else:
            return arr
        
    # JUST GUESSING ABOUT USING NONE IN REHEAP

###########

#import sys

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)

#######
h = Heap()
for x in a:
    h.add(x)
    print(h.median())



'''
Test case 0:
---
Your code did not pass this test case.

Input (stdin)

10
1
2
3
4
5
6
7
8
9
10

Your Output (stdout)
~ no response on stdout ~

Expected Output

1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
5.5

Compiler Message

Runtime Error

Error (stderr)

Traceback (most recent call last):
  File "solution.py", line 72, in <module>
    print(h.median())
  File "solution.py", line 18, in median
    copy = self.heapsort(copy)
  File "solution.py", line 58, in heapsort
    if array[index] is not None:
IndexError: list index out of range

'''
