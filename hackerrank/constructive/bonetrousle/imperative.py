# Use k to setup S

# b - trips
def soln(n, stock, b): # todo prev
    if b == 1:
        if n in stock:
            return [n]
        else:
            return [] # -1 is stupid
    else: # b > 2
        # Dangerous!! 
        m = max(set(stock))
        rem = n
        ans = set([])
        moves = b
        while rem > 0 and moves > 0:
            if m <= n:
                rem = n - m
                stock.remove(m)
                ans.add(m)
                moves -= 1
            else:
                return None # TODO
        return ans

    return None

