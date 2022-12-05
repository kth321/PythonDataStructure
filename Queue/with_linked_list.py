from typing import Union, TypeVar

T = TypeVar('T', bound=Union[int, float])

class Node(object):
    def __init__(self, value: T=None):
        self.value = value
        self.left = self.right = None


class Queue(object):
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def isempty(self) -> bool:
        return self.length == 0

    def enque(self, item: T) -> None:
        if self.isempty():
            self.head = self.tail = Node(item)
        else:
            new_node = Node(item)
            new_node.left = self.tail.left
            self.tail.right = new_node
            self.tail = new_node
        self.length += 1
    
    def deque(self) -> T:
        if not self.isempty():
            item = self.head.value
            self.head = self.head.right
            self.head.left = None
            self.length -= 1
            return item
        raise IndexError("Sequence index out of range.")

    def front(self) -> T:
        if not self.isempty():
            return self.head.value
        raise IndexError("Sequence index out of range.")

    def size(self) -> int:
        return self.length


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enque(i)
    for i in range(10):
        print('size', queue.size())
        print(queue.deque())