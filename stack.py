# 栈后进先出


class Stack(object):

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        if self.stack:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

