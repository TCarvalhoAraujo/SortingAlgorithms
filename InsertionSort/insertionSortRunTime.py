import time
import random
import matplotlib.pyplot as plt

# Insertion sort implementation
def insertion_sort(array):
    # Loop over the array starting from the second element
    for i in range(1, len(array)):
        # Store the value to be inserted
        temp = array[i]
        j = i - 1

        # Move the elements that are greater than temp
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # Insert the element in the correct position
        array[j + 1] = temp

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
        
        # Perform the insertion sort
        insertion_sort(random_array)
        
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
