class BitArray():

    def __init__(self, n):
        # TODO test length non-neg

        self.length = n
        self.data   = [] if n == 0 else None 

    def __len__(self):
        return self.length

    def set(self, array):
        if len(array) != self.length:
            raise BadSet()

        self.data = array

    def array(self):
        if self.data is None:
            raise NoValue()
        else:
            return self.data

    # TODO __str__(self):
    
    def clear(self):
        self.data = [0] * self.length

    def num(self):
        #if self.length == 0:
        #    raise Bits.NoValue()
        #    # Or default to 0

        if self.data is None:
            raise NoValue()
        else:
            exp   = self.length - 1
            value = 0
            for bit in self.data:
                value += bit * 2**exp
                exp -= 1
            return value

class NoValue(Exception):
    pass

# TODO rename
# TODO split into Incomplete and Overflow
class BadSet(Exception):
    pass

class Bits(BitArray):
    # should this be the base class?...

    # Can you have a slice of a slice? No. Unneccessary.
    # But, we could have Bit have a slice() method

    def slice(self, low, high):
        '''
        Get a slice of bits that is still mapped back to the main object.
        '''
        # Can't just return a slice...
        # Can't return a new Bit object either, as this would make a
        # copy... right?

        new = Slice(low, high, self)
        new.data = self.data[low:high + 1]
        return new

class Slice(BitArray):
    # Has more adv. set method
    def __init__(self, low, high, parent):
        self.parent = parent
        self.low    = low
        self.high   = high
        self.size   = 1 + high - low 

    def set(self, array):
        if len(array) != self.size:
            raise BadSet()

        # rebinds:
        # self.data = array
        for i in list(range(0, len(array))):
            self.parent.data[i] = array[i]
         

