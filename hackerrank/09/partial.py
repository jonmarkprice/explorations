from functools import reduce

'''Trie without keys, support parial finds'''
class PartialTrie():
    def __init__(self):
        self.head = Node()
    
    def count(self, keys, verbose=False):
        return len(self.find(keys, verbose))
    
    # replace results with int
    def find(self, keys, verbose=False):
        node    = self.head
        results = []
        # I did not design this to keep going!!!
        for i in range(len(keys)):
            index   = self.index(keys[i])
            new     = node.nodes[index]
            if new is None:
                print('None! Key = ' + keys[i])
            #    return []
            else:
                #if new.end:
                #    results.append(keys[:i + 1])
                #    if verbose:
                #        print('Adding ' + keys[i] + ' to results')
                #elif verbose:
                #    print(keys[i] + ' is not leaf. continuing.')
                node = new
        
        # Get all the results
        # recursive
        # TODO see keytrie.py :: __find
        
        
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

