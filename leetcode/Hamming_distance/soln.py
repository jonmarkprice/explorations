from math import floor, log

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        x_bits = self.get_bits(x)
        y_bits = self.get_bits(y)
        shorter_length = min(len(x_bits), len(y_bits))
        
        for i in range(0, shorter_length):
            if x_bits[i] != y_bits[i]:
                distance += 1

        # deal with the remainder
        if len(x_bits) > len(y_bits):
            longer = x_bits
        elif len(x_bits) < len(y_bits):
            longer = y_bits
        else:
            return distance

        # Assume shorter list is 0-padded
        for i in range(shorter_length, len(longer)):
            if longer[i] is True:
                distance += 1

        return distance

    def get_bits(self, n):
        # return a list of booleans
        if n == 0:
            return [False]

        # Setup
        k = int(floor(log(n, 2)))
        bits = [False] * (k + 1)
        
        # First iteration
        bits[k] = True
        rem = n - 2**k

        while rem != 0:
            k = int(floor(log(rem, 2))) # same problem again
            bits[k] = True
            rem = rem - 2**k
        
        return bits
