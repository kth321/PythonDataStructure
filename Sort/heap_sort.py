import heapq

def heap_sort1(seq):
    h = []
    for i in seq:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == '__main__':
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    print(heap_sort1(seq))