from functools import reduce

'''Trie without keys, support partial finds'''
class PartialTrie():
    def __init__(self):
        self.head = Node()
    
    def __str__(self):
        return str(self.head)

    """
    I would like a the trie to be ordered and intented, so that
    'abc'
    'abs'
    'bsd'
    would display as:
        a
            [a]b
                [ab]c
                [ab]s
        b
            [b]s
                [bs]d
    """
        
    
    def count(self, keys):
        if len(keys) == 0:
            return 0
        node    = self.head
        results = 0
        for i in range(0, len(keys) - 1):
            index   = self.index(keys[i])
            new     = node.nodes[index]
            if new is not None:
                node = new
            else:
                return 0
        last = self.index(keys[-1])
        if node.nodes[last] is not None:
            results = node.nodes[last].count
        return results

    def find(self, keys, verbose=False):
        if len(keys) == 0:
            return []
        node    = self.head
        results = []
        for i in range(0, len(keys) - 1):
            index   = self.index(keys[i])
            if verbose:
                print('Interpretting {} as {}'.format(keys[i], index))
            new     = node.nodes[index]
            if verbose:
                j = 0
                for k in node.nodes:
                    print('{}: {}'.format(j, k))
                    j += 1
            #if new is None:
            #    print('None! Key = ' + keys[i])
            #else:
            if new is not None:
                node = new
        
        # Search last key:
        if verbose:
            print('searching for {0}'.format(keys[-1]))
        
        last = self.index(keys[-1])
        if node.nodes[last] is not None:
            if node.nodes[last].end:
                results.append(keys)
            elif verbose:
                print('"{0}" not an end node'.format(keys))
            results += self.get_all(node.nodes[last], keys, verbose)
            if verbose:
                print(results)
        return results
        
    def get_all(self, head, keys, verbose=False):
        results = []
        for i in range(len(head.nodes)):
            if verbose:
                print('.', end='')
            if head.nodes[i] is not None:
                new_keys = keys + chr(i + 97)
                if head.nodes[i].end:
                    results.append(new_keys)
                results += self.get_all(head.nodes[i], new_keys)
        return results

    def index(self, char):
        code = ord(char)
        if (code >= 97) and (code <= 122):
            return code - 97
        else:
            raise Exception('Key not in range')

    def add(self, keys):
        node = self.head
        for i in range(0, len(keys)):
            index = self.index(keys[i])
            if node.nodes[index] is None:
                node.nodes[index] = Node()
            if i == len(keys) - 1:
                node.nodes[index].end = True
            #print(chr(index + 97) + ': ' + str(node.nodes[index].count))
            node.nodes[index].count += 1
            #print(chr(index + 97) + ': ' + str(node.nodes[index].count))
            node = node.nodes[index]

class Node():
    def __init__(self):
        self.nodes  = [None] * 26
        self.end    = False
        self.count  = 0

    def __len__(self):
        none_filter = lambda acc, new: acc + (0 if new is None else 1)
        return reduce(none_filter, self.nodes, 0)

    def __str__(self):
        s = '['
        s += 'end: ' + str(self.end) + ', '
        s += 'nodes: ' + str(len(self)) + ', '
        s += 'count: ' + str(self.count) + ', ['
        for i in range(len(self.nodes)):
            if self.nodes[i] is not None:
                s += '\n'
                s += chr(i + 97) + ': ' + str(self.nodes[i])
        s += ']]'
        return s

