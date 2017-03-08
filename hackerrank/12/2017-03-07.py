def merge(a, b):
    
    # This is the problem step. DOn't do it!
    c = a + b #list
    
    
    i = 0
    j = len(a) # first item of b
    inv = 0
    
    while i < j:
        if j >= len(c):
            break

        if c[i] > c[j]:
            # successively swap
            k = j
            
            # what if we just return set 
            # inv += j - i 
            # then a to result...
            while k > i:
                # swap
                c[k], c[k - 1] = c[k - 1], c[k]
                k -= 1
                inv += 1
            j += 1
        i += 1
    return (c, inv)

# initial call: start = 0, end = len(a) - 1
def mergesort(a): #, start=None, end=None):
#    if start is None:
#        start = 0
#    if end is None:
#        end = len(a) - 1
    
    mid = (len(a) - 1) // 2
    # for len // 2:
    # 1 // 2 = 0 : [0^]
    # 2 // 2 = 1 : [0, 1^]
    # 3 // 2 = 1 : [0, 1^, 2]
    # 4 // 2 = 2 : [0, 1, 2^, 3]
    
    # for (end - start // 2):
    #len = 1 : 0 - 0 // 2 => 0 [0^]
    #len = 2 : 1 - 0 // 2 => 1 [0^, 1]
    #len = 3 : 2 - 0 // 2 => 1 [0, 1^, 2]
    #len = 4 : 3 - 0 // 2 => 1 [0, 1^, 2, 3]
    #if start == end:
    if len(a) == 1:
        #return (a[start:start + 1], 0)
        return (a[0:1], 0)
    else:
        left, m = mergesort(a[:mid + 1]) #, start, mid)
        right, n = mergesort(a[mid + 1:]) #, mid + 1, end) # inclusive
        #return (merge(left, right), m + n)
        array, inv = merge(left, right)
        return (array, m + n + inv)
        
    # Choose to pass indices or sub-lists
    # merge deals with sublists (c = a + b)
    # mergesort deals with indices

if __name__ == '__main__':
    print(mergesort([1]))
    print(mergesort([0, 1]))
    print(mergesort([1, 0]))
    print(mergesort([1, 8, 5, 1]))
    print(mergesort([2, 1, 3, 1, 2]))
