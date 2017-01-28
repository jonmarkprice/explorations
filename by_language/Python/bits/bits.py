class BitArray():

    def __init__(self, n):
        # TODO test length non-neg
        self.length = n

        # XXX this will make Bit(_).slice(_,_) fail because we cannot
        # subscript None
        # self.data   = [] if n == 0 else None 

        # XXX this is hard to test for
        self.data   = [] + [None] * n

    def __len__(self):
        return self.length

    def set(self, array):
        if len(array) != self.length:
            raise BadSet()

        self.data = array

    def array(self):
        if any(bit is None for bit in self.data):
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

        if (self.data == [] 
            or any(bit is None for bit in self.data)): 
            raise NoValue()
        else:
            return num_from_array(self.data)
class NoValue(Exception):
    pass

# TODO split into Incomplete and Overflow
class BadSet(Exception):
    pass

class Bits(BitArray):
    # Can you have a slice of a slice? No. Unneccessary.
    # But, we could have Bit have a slice() method

    # It is possible that this simply won't work both ways...
    # in that case, use "snapshots" instead of slices...
    def slice(self, low, high):
        '''
        Get a slice of bits that is still mapped back to the main object.
        '''

        new = Slice(low, high, self)
        # This was failing if Bits is uninitiated, i.e. self.data == None
        # Instead made self.data an array of None's of the correct size.
        new.data = self.data[low:high + 1]
        return new

class Slice(BitArray):
    '''
    BitArray subclass that deals with updating the given slice of
    data from its parent.
    '''
    def __init__(self, low, high, parent):

        # TODO: why does self.parent = parent 'work' but 
        # self.data = self.parent.data not work?
        self.parent = parent
        self.low    = low
        self.high   = high
        self.size   = 1 + high - low 

    def set(self, array):
        if len(array) != self.size:
            raise BadSet()

        # Need to iterate so we don't rebind
        # i.e. we can't just do:
        #   self.parent.data = array
        # as this would simply make self.parent.data
        # point to array.
        for i in list(range(0, len(array))):
            self.parent.data[i] = array[i]

    def array(self):
        return self.parent.data[self.low:self.high + 1]

    # XXX Duplication
    # This is largely shared anyway...
    def num(self):
        if (self.parent.data == [] 
            or any(bit is None for bit in self.parent.data)): 
            raise NoValue()
        else:
            return num_from_array(self.parent.data) 

def num_from_array(array):
    exp   = len(array) - 1
    value = 0
    for bit in array:
        value += bit * 2**exp
        exp -= 1
    return value


