import sys
from typing import Union, TypeVar, List

sys.setrecursionlimit(10_000)

T = TypeVar('T', bound=Union[int, float])

def binary_search(arr: List[T], target: T) -> int:
    def bs(left: int=0, right: int=len(arr) - 1):
        mid = (right - left) //2 + left
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return bs(mid + 1, right)
        else:
            return bs(left, mid - 1)
    return bs()

if __name__ == '__main__':
    arr = [11, 15, 28, 44, 57]
    for i in arr:
        print(binary_search(arr, i))