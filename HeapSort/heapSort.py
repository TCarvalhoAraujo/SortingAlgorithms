def heapify(array, n, i):
    largest = i #initialize largest as root
    left_child = 2 * i + 1 #left child index
    right_child = 2 * i + 2 #right child index

    #if the left child is larger than the root
    if left_child < n and array[left_child] > array[largest]:
        largest = left_child

    #if the right child is larger than the current largest
    if right_child < n and array[right_child] > array[largest]:
        largest = right_child

    #if the largest element is not the root
    if largest != i:
        array[i], array[largest] = array[largest], array[i] #swap

        #recursively heapify the affected subtree
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)

    #build max heap
    #n // 2 - 1 -> gets the last non-leaf node (because leaf-nodes don't have child nodes)
    #-1 -> the loop will go until it reaches -1
    #-1 -> decrement by 1 each iteration
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    #extract elements one by one from the heap
    #n - 1 -> last element of the array
    #0 -> the loop will stop before it reaches the first element
    #-1 -> decrement by 1 each iteration
    for i in range(n - 1, 0, -1):
        #move the current root to the end
        array[i], array[0] = array[0], array[i]

        #heapify the reduced heap
        heapify(array, i, 0)

unordered_array = [4, 2, 6, 5, 1, 3]

#printing unordered array
print("Unordered array: " + str(unordered_array))

heap_sort(unordered_array)

#printing ordered array
print("Ordered array: " + str(unordered_array))