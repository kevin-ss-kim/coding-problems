class QueueWithTwoStacks(object):

    def __init__(self):
        self.stack1 = [] # "IN" stack
        self.stack2 = [] # "OUT" stack

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) == 0:
            raise IndexError("Can't dequeue from empty queue")
        while len(self.stack1) > 0:
            new_stack_item = self.stack1.pop()
            self.stack2.append(new_stack_item)
        return self.stack2.pop()