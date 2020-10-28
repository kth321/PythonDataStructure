def sequential_search(seq, x):
    for i in seq:
        if i == x:
            return True
    return False

def ordered_sequential_search(seq, x):
    for i in seq:
        if i > x:
            return False
        if i == x:
            return True
    return False
        

if __name__ == '__main__':
    seq = [1,5,6,8,3]
    x1 = 5
    x2 = 7
    print(sequential_search(seq, x1))
    print(sequential_search(seq, x2))