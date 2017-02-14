from functools import reduce

'''Trie without keys, support parial finds'''
class PartialTrie():
    def __init__(self):
        self.head = Node()
    
    def count(self, keys, verbose=False):
        return len(self.find(keys, verbose))
    
    # replace results with int
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
            if new is None:
                print('None! Key = ' + keys[i])
            else:
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
        for i in range(len(keys)):
            index = self.index(keys[i])
            if node.nodes[index] is None:
                node.nodes[index] = Node()
            if i == len(keys) - 1:
                node.nodes[index].end = True
            node = node.nodes[index]

    def print_trie(self):
       print(self.head)

class Node():
    def __init__(self):
        self.nodes  = [None] * 26
        self.end    = False

    def __len__(self):
        none_filter = lambda acc, new: acc + (0 if new is None else 1)
        return reduce(none_filter, self.nodes, 0)

    def __str__(self):
        s = '['
        s += 'end: ' + str(self.end) + ', '
        s += 'nodes: ' + str(len(self)) + ', ['
        for i in range(len(self.nodes)):
            if self.nodes[i] is not None:
                s += '\n'
                s += chr(i + 97) + ': ' + str(self.nodes[i])
        s += ']]'
        return s

