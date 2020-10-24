def selection_sort(seq):
    length = len(seq) - 1
    for i in range(length):
        min_v = i
        for j in range(i+1, length+1):
            if seq[min_v] > seq[j]:
                min_v = j
        seq[min_v], seq[i] = seq[i], seq[min_v]
    return seq

if __name__ == '__main__':
    seq = [11,3,28,43,9,4]
    print(selection_sort(seq))