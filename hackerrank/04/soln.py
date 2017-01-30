#A Node is defined as: 
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

""" DEPRECATED
class TaggedNode(node):
    def __init__(self, node):
        self.node = node
        #self.tag  = False
        self.visited = False
"""

def has_cycle(current):
    #visited = []
    visited = dict()
    while current is not None:
        if current in visited:
            return True
        else:
            #visited.append(current)
            visited[current] = True
            current = current.next
    return False


