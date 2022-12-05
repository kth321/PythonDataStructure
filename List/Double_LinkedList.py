from typing import TypeVar, Union

T = TypeVar("T", bound=Union[int, float])

class Node(object):
    def __init__(self, value=None):
        self.left = self.right = None
        self.value = value


class DLL(object):
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def isempty(self) -> bool:
        return self.length == 0

    def add_first(self, item: T) -> None:
        node = Node(item)
        if self.isempty():
            self.head = self.tail = node
        else:
            node.right = self.head
            self.head = node
            self.head.left = node
            self.head = node
        self.length += 1

    def add_last(self, item: T) -> None:
        node = Node(item)
        if self.isempty():
            self.head = self.tail = node
        else:
            node.left = self.tail
            self.tail.right = node
            self.tail = node
        self.length += 1

    def insert(self, pos: int, item: T) -> None:
        if pos == 0:
            self.add_first(item)
        elif pos == -1 or pos == self.length:
            self.add_last(item)
        else:
            if pos > self.length:
                raise IndexError("Sequence index out of range.")
            else:
                cnt = 0
                node = self.head
                while node:
                    if cnt == pos - 1:
                        new_node = Node(item)
                        new_node.right = node.right
                        node.right.left = new_node
                        node.right = new_node
                        new_node.left = node
                        self.length += 1
                        return
                    cnt += 1
                    node = node.right
                raise IndexError("Sequence index out of range.")

    def remove_first(self) -> bool:
        if not self.isempty():
            if self.length == 1:
                self.head = self.tail = None
                self.length = 0
            else:
                self.head = self.head.right
                self.head.left = None
                self.length -= 1
                return True
        else:
            raise IndexError("Sequence index out of range.")
    
    def remove_last(self) -> bool:
        if not self.isempty():
            if self.length == 1:
                self.head = self.tail = None
                self.length = 0
            else:
                self.tail = self.tail.left
                self.tail.right = None
                self.length -= 1
                return True
        else:
            raise IndexError("Sequence index out of range.")

    def remove(self, pos: int) -> bool:
        if not self.isempty():
            if pos == 0:
                self.remove_first()
            elif pos == -1 or pos == self.length - 1:
                self.remove_last()
            else:
                node = self.head
                cnt = 0
                while node:
                    if cnt == pos - 1:
                        node.right = node.right.right
                        node.right.left = node
                        self.length -= 1
                        return True
                    cnt += 1
                    node = node.right
                raise IndexError("Sequence index out of range.")
        else:
            raise IndexError("Sequence index out of range.")

    def search_target(self, target: T) -> int:
        if not self.isempty():
            node = self.head
            cnt = 0
            while cnt < self.length:
                if node.value == target:
                    return cnt
                cnt += 1
                node = node.right
            raise ValueError("Inappropriate argument value")
        else:
            raise ValueError("Inappropriate argument value")

    def search_pos(self, pos: int) -> T:
        if not self.isempty():
            node = self.head
            cnt = 0
            while pos < self.length:
                if pos == cnt:
                    return node.value
                cnt += 1
                node = node.right
            raise IndexError("Sequence index out of range.")
        else:
            raise IndexError("Sequence index out of range.")

    def size(self):
        return self.length

    def print(self):
        if not self.isempty():
            node = self.head
            while node:
                print(node.value, end=' ')
                node = node.right
            print()
        else:
            print('List is empty')


if __name__ == "__main__":
    list = DLL()
    # list.add_first(5)
    # list.add_first(10)
    # list.add_last(20)
    # list.add_last(30)
    # list.insert(5, 3)

    list.insert(0, 10)
    list.add_first(20)
    list.insert(0, 30)
    list.add_last(40)
    list.print()
    list.remove(3)
    list.print()
    print(list.search_target(2))
    print(list.size())