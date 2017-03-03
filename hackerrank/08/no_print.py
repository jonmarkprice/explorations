# Following a "by-example" approach

class Heap():
    def __init__(self, array=[]):
        self.array = array

    def heapify(self, index=0):
        if self.array == []:
            return
        
        left  = 2 * index + 1
        right = 2 * index + 2
        parent = (index - 1) // 2
        value = self.array[index]
        last  = self.size() - 1
        assert last >= index

        # Compare to childen
        if last >= right: # Both children are there
            if value < min(self.array[left], self.array[right]):
                # Check both children
                self.heapify(left)
                self.heapify(right)
            elif self.array[left] < self.array[right]:
                self.swap(index, left)
                if index != 0:
                    self.heapify(parent)
                else:
                    self.heapify(index)
            else:
                self.swap(index, right)
                if index != 0:
                    self.heapify(parent)
                else:
                    self.heapify(index)
        elif last == left:
            # Only one child
            if value > self.array[left]:
                self.swap(index, left)
                if index != 0:
                    self.heapify(parent)
                else:
                    self.heapify(index)

    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def add(self, value):
        self.array.append(value)

    def pop(self):
        if self.array == []:
            return None
        popped = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.heapify()
        return popped
        
    def size(self):
        return len(self.array)
        
    def sort(self):
        in_order = []
        n = self.size()
        self.heapify()
        for i in range(0, n):
            in_order.append(self.pop())
        self.array = in_order

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def median(array):
    n = len(array)
    if even(n):
        return (array[(n // 2) - 1] + array[n // 2]) / 2.0
    else:
        return float(array[n // 2])

if __name__ == '__main__':
    h = Heap()

    n = int(input().strip())
    a = []
    a_i = 0
    for a_i in range(n):
       a_t = int(input().strip())
       a.append(a_t)
       h.add(a_t)
       h.sort()
       print(median(h.array))
