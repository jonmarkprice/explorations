def rot1(array): # start with something simple
    return rot(1, array)

def rot(k, a):
    return array_left_rotation(a, len(a), k)

def array_left_rotation(a, n, k):
    new = [None] * n

    for index in list(range(0, n)):
    #if index != 0: 
        if index - k >= 0: # more generalizable
            # Copy to new array
            # TODO: do in-place
            new[index - k] = a[index]
        else:
            # this needs to scale with k
            new[n - k + index] = a[index]
    return new

### From hackerrank
def run():
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k);
    print(*answer, sep=' ')


