from typing import Union, TypeVar

T = TypeVar('T', bound=Union[int, float])

class Stack(object):
    def __init__(self):
        self.stk = []

    def isempty(self) -> bool:
        return not bool(self.stk)
    
    def push(self, item: T) -> None:
        self.stk.append(item)
    
    def pop(self) -> T:
        return self.stk.pop()
    
    def peek(self) -> T:
        if not self.isempty():
            return self.stk[-1]
        raise IndexError("Sequence index out of range.")

    def size(self) -> int:
        return len(self.stk)

