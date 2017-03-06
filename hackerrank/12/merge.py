def mergesort(a, i, k):
    if len(a) == 1:
        return a, 0
    else:
        # probably too slow
        mid = (k // 2) + 1
        left, n = mergesort(a, 0, mid)
        right, m = mergesort(a, mid, k)
        return merge(left, right), m + n

def merge(a, b):
    n = len(a) + len(b)
    c = a + b
    inv = 0
    swapped = True #default for first iteration
    while swapped:
        # Single pass
        swapped = False
        for i in range(0, n - 1):
            if c[i] > c[i + 1]:
                swapped = True
                c[i], c[i + 1] = c[i + 1], c[i]
                inv += 1
    return c, inv

def count_inversions(a):
    _, inv = mergesort(a, 0, len(a))
    return inv

d = int(input().strip())
for a0 in range(d):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))
