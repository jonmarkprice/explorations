from bits import Bits

### Helper functions ###
def reg(bit_slice):
    return 'R' + str(bit_slice.num())

### 
inst    = Bits(8)
opcode  = inst.slice(0, 3)
a       = inst.slice(4, 5)
b       = inst.slice(6, 7)

opcode.set([0, 0, 0, 0])
a.set([0, 1])
b.set([1, 1])
 
if opcode.array() == [0, 0, 0, 0]:
   print('AND {} {}'.format(reg(a), reg(b)))

else:
    # XXX something is wrong with multiple slices... 
    # write new unit test
    print(opcode.array())


