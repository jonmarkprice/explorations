# Following a "by-example" approach
dbg = False

class Heap():
    #def __init__(self, n):
    #    assert n > 0
    #    self.array  = [0] * n
    #    self.start  = n - 1
    #    self.END    = n - 1 # Constant
        
    def __init__(self, array=[]):
        self.array = array

    def reheap(self, verbose=dbg):
        last  = len(self.array) - 1
        index = 0
        
        while index < last:
            left  = 2 * index + 1
            right = 2 * index + 2
            value = self.array[index]

            # Compare to childen
            if right <= last: # Both children are there
                if value <= min(self.array[left], self.array[right]):
                    # No swap necessary, the heap property is in place.
                    if verbose:
                        print("Heap property restored.")
                    return

                elif self.array[left] < self.array[right]:
                    # We swapped with the smaller element, therefore, we only 
                    # need to check the swapped element's children
                    if verbose:
                        self.print_array(index)
                        print('Swap {} and {}'.format(value, self.array[left]))
                    self.swap(index, left)
                    index = left

                else:
                    # Swap and back to sqaure #1
                    if verbose:
                        self.print_array(index)
                        print('Swap {} and {}'.format(value, self.array[right]))
                    self.swap(index, right)
                    index = right

            # Special cases: 
            elif left == last:
                # Only one child
                if value <= self.array[left]:
                    if verbose:
                        print("Heap property restored.")
                    return
                else:
                    if verbose:
                        self.print_array(index)
                        print('Swap {} and {}'.format(value, self.array[left]))
                    self.swap(index, left)
                    #index = left
                    return # this was the last child
            else:
                # Last element
                return

    # log(n) worst case, i.e. if new node needs to be the head.
    def shift_up(self):
        last = len(self.array) - 1
        index = last
        while index > 0:
            parent = (index - 1) // 2
            if self.array[index] < self.array[parent]:
                # Heap property is violated
                self.swap(index, parent)
                index = parent # check parent's parent
            else:
                # Heap property is intact and we are guarenteed that still holds
                return

    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def add(self, value):
        self.array.append(value)
        self.shift_up()

    def pop(self, verbose=False):
        if self.array == []:
            return None
        if verbose:
            print(self.array)
        popped = self.array[0]
        
        # Replace with last element, or itself if len == 1, then pop
        self.array[0] = self.array[-1]
        self.array.pop() # or del
        
        self.reheap()
        return popped
        
    def size(self):
        return len(self.array)

    def print_array(self, index):
        n = len(self.array)
        s = '['
        s += ', '.join(str(self.array[i]) for i in range(0, index))
        s += '[{}]'.format(self.array[index])
        s += ', '.join(str(self.array[i]) for i in range(index + 1, n))
        s += ']'
        print(s, end='')
        
    def sort(self):
        in_order = []
        n = self.size()
        for i in range(0, n):
            in_order.append(self.pop())
        self.array = in_order

def median(array):
    n = len(array)
    if n % 2 == 0:
        return (array[(n // 2) - 1] + array[n // 2]) / 2.0
    else:
        return float(array[n // 2])

if __name__ == '__main__':
    n = int(input().strip())
    h = Heap()
    a = []
    a_i = 0
    for a_i in range(n):
        a_t = int(input().strip())
        a.append(a_t)
        h.add(a_t)
        h.sort()
        if dbg:
            print('input  : ' + str(a))
            print('sorted : ' + str(h.array))
        print(median(h.array))
    if dbg:
        print("Input was: " + str(a))
