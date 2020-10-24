def insertion_sort(seq):
    length = len(seq)
    for i in range(1, length):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

if __name__ == '__main__':
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    print(insertion_sort(seq))    