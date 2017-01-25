from functools import reduce

AND = 0b000
R = [None, None]
R[0] = 0b1010
R[1] = 0b1100

print(bin(R[0] & R[1]))

def AND(x, y):
    return bin(x & y)

# alternatively, use arrays of binary numbers..
instr = [0] * 10
if instr[0:4] == [0, 0, 0, 0]:
    print('and!')

def toNum_it(arr):
    n = len(arr) - 1
    x = 0
    for elem in arr:
        x += elem * 2**n
        n -= 1
    return x

def toNum_rec(arr, acc=0):
    n = len(arr) - 1
    x = acc + arr[0] * 2**n
    if len(arr) == 1:
        return x
    else:
        return toNum_rec(arr[1:], x)

toNum = toNum_rec

### Test cases ###
# Singleton lists
assert toNum([0]) == 0
assert toNum([1]) == 1

# Short lists
assert toNum([0, 1]) == 1
assert toNum([1, 0]) == 0b10
assert toNum([1, 1]) == 0b11


if toNum(instr[0:4]) == 0b0000:
    print('and (again!)')

R = [[1,0,1], [0,0,0], [0,1,0], [0,0,0]]
i2 = [0, 0, 0, 1,   0, 0,   1, 0]
if toNum(i2[0:4]) == 0b0001:
    print('not!')
    print('operand: ' + str(toNum(R[toNum(i2[4:6])])))
    ans = list(map(lambda a: 0 if a == 1 else 1, R[toNum(i2[6:8])]))
    print(ans)

    

