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

unordered_array = [4, 2, 6, 5, 1, 3]

#printing unordered array
print("Unordered array: " + str(unordered_array))

sorted_array = merge_sort(unordered_array)

#printing ordered array
print("Ordered array: " + str(sorted_array))