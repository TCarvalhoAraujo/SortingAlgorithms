def insertion_sort(array):
    #loop over the array starting from the second element
    for i in range(1, len(array)):
        #store the value to be inserted
        temp = array[i]
        j = i - 1

        #move the elements that are greater than temp
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        #insert the element in the correct position
        array[j + 1] = temp

unordered_array = [4, 2, 6, 5, 1, 3]

#printing unordered array
print("Unordered array: " + str(unordered_array))

insertion_sort(unordered_array)

#printing ordered array
print("Ordered array: " + str(unordered_array))