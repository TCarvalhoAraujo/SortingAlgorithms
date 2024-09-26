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

unordered_array = [4, 2, 6, 5, 1, 3]
n = len(unordered_array)

#printing unordered array
print("Unordered array: " + str(unordered_array))

quick_sort(unordered_array, 0, n - 1)

#printing ordered array
print("Ordered array: " + str(unordered_array))