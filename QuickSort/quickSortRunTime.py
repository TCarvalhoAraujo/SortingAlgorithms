import time
import random
import matplotlib.pyplot as plt

def partition(array, low, high):
    pivot = array[high] #pivot element
    i = low - 1 #index of the smallest element

    #traverse the array
    for j in range(low, high):
        #if current element is smaller or equal to pivot
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i] #swap

    #swap
    array[i + 1], array[high] = array[high], array[i +1]

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        #p is the partition index
        p = partition(array, low, high)

        #recursively sort the elements before and after partition (p)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)

def analyze_sorting_runtime():
    # Array sizes:
    array_sizes = [3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8, 3**9, 3**10]
    runtimes = []
    
    for size in array_sizes:
        # Generate an array of random integers between 1 and 3**n
        random_array = [random.randint(1, 3**10) for _ in range(size)]
        
        # Record the start time
        start_time = time.time()

        # Get last index
        n = len(random_array)
        
        # Perform the quick sort
        quick_sort(random_array, 0, n - 1)
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the time taken
        runtime = end_time - start_time

        # Add data to plot the graph later
        runtimes.append(end_time - start_time)
        
        # Print results
        print(f"Array size: {size}, Time taken: {runtime:.8f} seconds")

    # Plotting the bar graph
    plt.bar([str(size) for size in array_sizes], runtimes)
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort Runtime Analysis')
    plt.show()

# Running the function to analyze sorting runtime
analyze_sorting_runtime()