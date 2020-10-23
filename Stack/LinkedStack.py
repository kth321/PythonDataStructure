class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isempty(self):
        return not bool(self.head)
    
    def push(self, item):
        self.head = Node(item, self.head)
        self.length += 1
    
    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.length -= 1
            return value
        else:
            print('stack is empty')
            return False
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            print('stack is empty')
            return False

    def size(self):
        return self.length

if __name__ == '__main__':
    stack = Stack()
    print('stack is empty: ', stack.isempty())
    stack.push(1); print('peek is', stack.peek())
    stack.push(3); print('peek is', stack.peek())
    stack.push(5); print('peek is', stack.peek())
    print('stack is empty: ', stack.isempty())
    print('stack size is', stack.size())
    stack.pop();    print('peek is', stack.peek())
    stack.pop();    print('peek is', stack.peek())
    stack.pop()   
    print('stack is empty: ', stack.isempty())
