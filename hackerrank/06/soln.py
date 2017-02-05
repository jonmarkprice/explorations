class MyQueue(object):
    def __init__(self):
        self.inbox  = []
        self.outbox = []
    # pop and peek could use a common fn "dump"

    def dump(self):
        while self.inbox != []:
            self.outbox.append(self.inbox.pop())

    def peek(self):
        if self.outbox == []:
            self.dump()
        if self.outbox == []:
            #raise Exception("I'm empty!")
            return None
        else:
            return self.outbox[-1]

    def pop(self):
        if self.outbox == []:
            self.dump()
        if self.outbox == []:
            #raise Exception("I'm empty!")
            return None
        else:
            return self.outbox.pop()

    def put(self, value):
        self.inbox.append(value)
