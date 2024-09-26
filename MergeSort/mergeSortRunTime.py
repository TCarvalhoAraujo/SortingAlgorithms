import time
import random
import matplotlib.pyplot as plt

def merge(array1, array2):
    #create a new array to hold the sorted elements
    combined_array = []
    i = j = 0
    
    #compare elements from both arrays and append the smaller element to the combined array
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined_array.append(array1[i])
            i += 1
        else:
            combined_array.append(array2[j])
            j += 1
    
    #add remaining elements from array1
    while i < len(array1):
        combined_array.append(array1[i])
        i += 1

    #add remaining elements from array2
    while j < len(array2):
        combined_array.append(array2[j])
        j += 1

    return combined_array

def merge_sort(array):
    #base case: if the array has only one element, return it (it's already sorted)
    if len(array) <= 1:
        return array
    
    #find middle index of the array
    middle_index = len(array) // 2

    #recursively divide and sort both halves of the arrays
    left = merge_sort(array[:middle_index])
    right = merge_sort(array[middle_index:])

    #merge the sorted halves and return the result
    return merge(left, right)

def analyze_sorting_runtime():
    # Array sizes:
    array_sizes = [3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8, 3**9, 3**10]
    runtimes = []
    
    for size in array_sizes:
        # Generate an array of random integers between 1 and 3**n
        random_array = [random.randint(1, 3**10) for _ in range(size)]
        
        # Record the start time
        start_time = time.time()
        
        # Perform the merge sort
        merge_sort(random_array)
        
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
    plt.title('Merge Sort Runtime Analysis')
    plt.show()

# Running the function to analyze sorting runtime
analyze_sorting_runtime()