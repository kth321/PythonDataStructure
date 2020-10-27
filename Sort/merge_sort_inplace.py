def merge_sort_inplace(L1, L2):
    if not L1 or not L2:
        return L1 or L2
    L1 = L1 + [None] * len(L2)
    p2 = len(L2) - 1
    p1 = len(L1) - len(L2) - 1
    p12 = len(L1) - 1

    while p1 >= 0 and p2 >= 0:
        item_to_be_merged = L2[p2]
        item_being_merged = L1[p1]
        if item_being_merged > item_to_be_merged:
            L1[p12] = L1[p1]
            p1 -= 1
        else:
            L1[p12] = L2[p2]
            p2 -= 1
        p12 -= 1
    return L1

if __name__ == '__main__':
    L1 = [1,2,3,4,5,6,7]
    L2 = [2,4,5,8]
    print(merge_sort_inplace(L1, L2))