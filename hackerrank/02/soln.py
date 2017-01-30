def number_needed(a, b):
    a = list(a)
    b = list(b)
    number = 0
    
    a.sort()
    b.sort()
    while min(len(a), len(b)) > 0:
        if a[-1] == b[-1]:
            a.pop()
            b.pop()
        elif a[-1] > b[-1]:
            # drop a
            a.pop()
            number += 1
        elif a[-1] < b[-1]:
            b.pop()
            number += 1

    # for the remaining, add all
    number += max(len(a), len(b))
    
    return number
