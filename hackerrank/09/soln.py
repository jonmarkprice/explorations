from functools import reduce

class PartialTrie():
    def __init__(self):
        self.head = Node()

    # replace results with int
    def find(self, keys):
        if len(keys) == 0:
            return 0

        node    = self.head
        results = 0
        for i in range(0, len(keys) - 1):
            index   = self.index(keys[i])
            #if verbose:
            #    print('Interpretting {} as {}'.format(keys[i], index))
            new = node.nodes[index]
            if verbose:
                j = 0
                for k in node.nodes:
                    #print('{}: {}'.format(j, k))
                    j += 1
            #if new is None:
            #    print('None! Key = ' + keys[i])
            #else:
            node = new
        
        last = self.index(keys[-1])
        if node.nodes[last] is not None:
            if node.nodes[last].end:
                #results.append(keys)
                results += 1
            #elif verbose:
            #    print('"{0}" not an end node'.format(keys))
            results += self.get_all(node.nodes[last], keys)
            #if verbose:
            #    print(results)
        return results
        
    def get_all(self, head, keys):
        results = 0
        for i in range(len(head.nodes)):
            #if verbose:
            #    print('.', end='')
            if head.nodes[i] is not None:
                #new_keys = keys + chr(i + 97)
                if head.nodes[i].end:
                    #results.append(new_keys)
                    results += 1
                results += self.get_all(head.nodes[i], keys + chr(i + 97))
        return results

    def index(self, char):
        code = ord(char)
        if (code >= 97) and (code <= 122):
            return code - 97
        else:
            raise Exception('Key not in range')

    def add(self, keys):
        node = self.head
        for i in range(len(keys)):
            index = self.index(keys[i])
            if node.nodes[index] is None:
                node.nodes[index] = Node()
            if i == len(keys) - 1:
                node.nodes[index].end = True
            node = node.nodes[index]

class Node():
    def __init__(self):
        self.nodes  = [None] * 26
        self.end    = False

#####

p = PartialTrie()
t = int(input())
for line in range(t):
    op, contact = input().split(' ')
    if op == 'add':
        p.add(contact)
    elif op == 'find':
        res = p.find(contact)
        print(len(res))
    

