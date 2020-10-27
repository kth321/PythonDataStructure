# normal merge sort
def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    result = []
    while left and right:
        if left[-1] > right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return left or right + result