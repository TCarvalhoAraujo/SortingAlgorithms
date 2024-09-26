import time
import random
import matplotlib.pyplot as plt

def selection_sort(array):
    #iterates through the length of the array starting from the lowest element
    for i in range (len(array)):
        #assume the first element is the minimum
        min_index = i
        
        #iterate through the unsorted part of the array
        for j in range(i + 1, len(array)):
            
            #if a smaller element is found, update minIndex
            if array[j] < array[min_index]:
                min_index = j

        #if the smallest element isn't already in place, swap it    
        if i != min:
            array[i], array[min_index] = array[min_index], array[i]

# Function to generate random arrays and measure runtime
def analyze_sorting_runtime():
    # Array sizes:
    array_sizes = [3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8, 3**9, 3**10]
    runtimes = []
    
    for size in array_sizes:
        # Generate an array of random integers between 1 and 3**n
        random_array = [random.randint(1, 3**10) for _ in range(size)]
        
        # Record the start time
        start_time = time.time()
        
        # Perform the selection sort
        selection_sort(random_array)
        
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