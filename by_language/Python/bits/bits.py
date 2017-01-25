class Bits():

    def __init__(self, n):
        # TODO test length non-neg

        self.length = n
        self.data   = [] if n == 0 else None 

    def __len__(self):
        return self.length

    def set(self, array):
        self.data = array

    def array(self):
        if self.data is None:
            raise Bits.NoValue()
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
            raise Bits.NoValue()
        else:
            exp   = self.length - 1
            value = 0
            for bit in self.data:
                value += bit * 2**exp
                exp -= 1
            return value

    class NoValue(Exception):
        pass
