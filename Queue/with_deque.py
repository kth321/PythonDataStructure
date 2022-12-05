from typing import Union, TypeVar
from collections import deque

T = TypeVar('T', bound=Union[int, float])
class Queue(object):
    def __init__(self):
        self.q = deque()
        self.length = 0

    def isempty(self) -> bool:
        return self.length == 0

    def enque(self, item: T) -> None:
        self.q.append(item)
        self.length += 1
    
    def deque(self) -> T:
        if not self.isempty():
            self.length -= 1
            return self.q.popleft()
        raise IndexError('Sequence index out of range.')
    
    def front(self) -> T:
        if not self.isempty():
            return self.q[0]
        raise IndexError('Sequence index out of range.')
    
    def size(self) -> int:
        return self.length


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enque(i)
    for i in range(10):
        print(queue.front())
        queue.deque()