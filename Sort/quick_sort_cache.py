def quick_sort(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    lower = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    upper = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort(lower) + [pivot] + quick_sort(upper)

if __name__ == '__main__':
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    print(quick_sort(seq))