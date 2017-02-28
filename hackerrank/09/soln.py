from partial import PartialTrie

p = PartialTrie()
t = int(input().strip())
for line in range(t):
    op, contact = input().strip().split(' ')
    if op == 'add':
        p.add(contact)
    elif op == 'find':
        print(p.count(contact))
