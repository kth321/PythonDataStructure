from typing import Union, TypeVar

T = TypeVar('T', bound=Union[int, float])

class Node(object):
    def __init__(self, value: T=None, next=None):
        self.value = value
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isempty(self) -> bool:
        return not bool(self.head)
    
    def push(self, item:T) -> None:
        self.head = Node(item, self.head)
        self.length += 1
    
    def pop(self) -> T:
        if not self.isempty():
            value = self.head.value
            self.head = self.head.pointer
            self.length -= 1
            return value
        raise IndexError('Sequence index out of range.')
    
    def peek(self) -> T:
        if not self.isempty():
            return self.head.value
        raise IndexError('Sequence index out of range.')

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
