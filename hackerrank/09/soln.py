class KeyTrie():
    def __init__(self):
        #self.nodes = []
        self.head = Node()
    
    def __find(self, head, key):
        # key is a string
        # first character is taken, rest is recurred with
        if len(key) > 0:
            index   = self.index(key[0])
            rest    = key[1:]
            node    = head.nodes[index]
            
            print('key: "' + str(key) + '"')
            print('index: "' + str(index) + '"')
            print('rest: "' + str(rest) + '"')
            
            print('node value: ' + str(node.value))
            print('node end: ' + str(node.end))
            print('node children: ' + str(len(node.nodes)))
            
            if node.end and rest == '':
                return node.value

            elif rest != '':
                return self.__find(node, rest)
            else:
                print('wtf')
        else:
            print('key "' + str(key) + '" not found at: ')
            print(node.end)
            print(node.value)

    def index(self, char):
        code = ord(char)
        #if code in range(97, 123): # Constant time?
        if (code >= 97) and (code <= 122):
            return code - 97
            #return (True, code - 97)
        else:
            raise Exception('Key not in range')
            #print('Key not in range')
            #return (False, None)

    def addNode(self, keys, node):
        self.__addNode(keys, node, self.head)

    def __addNode(self, keys, node, root):
        if len(keys) > 0:
            index = self.index(keys[0])
            if len(keys) == 1:
                # Insert (or update!) the desired node
                root.nodes[index] = node
                # Mission accomplished
            else:
                if root.nodes[index] is None:
                    # Add new "intermediate" nodes
                    root.nodes[index] = Node()
                # Recur
                self.__addNode(keys[1:], node, root.nodes[index])
        else:
            raise Exception('Empty key!')
        ''' Iterative solution
        root = ...
        i = 0
        for key in list(keys):
            i += 1
            if i == len(keys):
                self.head.nodes[self.index(key)] = node
                node.end = True
            else:
                self.head.nodes[self.index(key)] = Node()
        '''

    def find(self, key):
        return self.__find(self.head, key)

class Node():
    def __init__(self, value=None):
        self.nodes  = [None] * 26
        if value is not None:
            self.value  = value
            self.end    = True
        else:
            self.value  = None
            self.end    = False
