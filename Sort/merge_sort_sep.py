def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result

if __name__ == '__main__':
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    print(merge_sort(seq))