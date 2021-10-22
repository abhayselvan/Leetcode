class Heap:

    def __init__(self, array):

        self.size = len(array) + 1
        self.heap = self.createHeap([None] + array)
        print(self.heap[1:])


    def createHeap(self, array):

        if not array:
            return []

        for i in reversed(range(1, self.size//2)):
            self.heapify(i, 2*i, 2*i+1, array)

        return array


    def heapify(self, parent, leftChild, rightChild, array):

        while array[parent] > array[leftChild] or array[parent] > array[rightChild]:
            
            if array[leftChild] < array[rightChild]:
                array[leftChild], array[parent] = array[parent], array[leftChild]
                parent = leftChild
            else:
                array[rightChild], array[parent] = array[parent], array[rightChild]
                parent = rightChild
            leftChild, rightChild = 2*parent, 2*parent+1

            if rightChild >= self.size:
                break


    def heapPush(self, element):

        self.heap.append(element)

        child, parent = self.size, self.size//2

        while self.heap[child] < self.heap[parent]:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child] 
            child, parent = parent, parent//2
            if parent < 1:
                break

        self.size += 1
        print(self.heap[1:])

    def heapPop(self):

        self.heap[1], self.heap[self.size-1] = self.heap[self.size-1], self.heap[1]
        minElement = self.heap.pop()

        self.heapify(1, 2, 3, self.heap)
        print(self.heap[1:])
        return minElement





heap = Heap([5,4,3,2,1])
heap.heapPush(-2)
print(heap.heapPop())


        

