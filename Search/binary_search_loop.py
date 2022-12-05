from typing import Union, TypeVar, List

T = TypeVar('T', bound=Union[int, float])

def binary_search(arr: List[T], target: T) -> int:
    left, right = 0, len(arr)
    while left <= right:
        mid = (right - left) // 2 + left
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    arr = [11, 15, 28, 44, 57]
    for i in arr:
        print(binary_search(arr, i))