"""
A (binary) heap data structure is an array object seen as 
a nearly complete binary tree where
- each node is associated with an element of the array
- heap-size is the attribute that represents the number of elements in array A
- each parent node has two children nodes

Two types of binrary heaps which satisfies a heap property
- max-heaps: A[parent(i)] >= A[i]
- min-heaps: A[parent(i)] <= A[i]

Methods
- max-heapify: maintain max-heap property
- build-max-heap: produces a max-heap from an unordered input array
- heapsort: sorts an array in place
"""
class MaxHeap:
    def __init__(self, A):
        self.heap_size = len(A)
        self.parent_node = (self.heap_size) // 2 # start at the midpoint
        print(f"{self.parent_node = }")
        self.A = A
   
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def max_heapify(self, A, i):
        largest = i
        l = self.left(i)
        r = self.right(i)
        print(f"Left node: {l}")
        print(f"Right node: {r}\n")
        if l < self.heap_size and A[l] >= A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and A[r] >= A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)
    
    def build_max_heap(self):
        for i in range(self.parent_node - 1, -1, -1):
            print(f"{i = }")
            self.max_heapify(self.A, i)
            print(f"{self.A = }")
        return self.A

class Heapsort(MaxHeap):
    def __init__(self, A):
        super().__init__(A)
    
    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.A) - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size = i
            self.max_heapify(self.A, 0)
        return self.A

# Test the heap sort implementation
if __name__ == "__main__":
    test_array = [4, 10, 3, 5, 1, 8, 7]
    heapsort = Heapsort(test_array)
    print("Original array:", test_array)
    sorted_array = heapsort.heap_sort()
    print("Sorted array:", sorted_array)