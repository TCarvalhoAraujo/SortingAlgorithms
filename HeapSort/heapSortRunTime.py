import time
import random
import matplotlib.pyplot as plt

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

def analyze_sorting_runtime():
    # Array sizes:
    array_sizes = [3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8, 3**9, 3**10]
    runtimes = []
    
    for size in array_sizes:
        # Generate an array of random integers between 1 and 3**n
        random_array = [random.randint(1, 3**10) for _ in range(size)]
        
        # Record the start time
        start_time = time.time()
        
        # Perform the heap sort
        heap_sort(random_array)
        
        # Record the end time
        end_time = time.time()

        # Add data to plot the graph later
        runtimes.append(end_time - start_time)
        
        # Calculate the time taken
        runtime = end_time - start_time
        
        # Print results
        print(f"Array size: {size}, Time taken: {runtime:.8f} seconds")

        # Plotting the bar graph
    plt.bar([str(size) for size in array_sizes], runtimes)
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Heap Sort Runtime Analysis')
    plt.show()

# Running the function to analyze sorting runtime
analyze_sorting_runtime()