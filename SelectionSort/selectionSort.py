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

unordered_array = [4, 2, 6, 5, 1, 3]

#printing unordered array
print("Unordered array: " + str(unordered_array))

selection_sort(unordered_array)

#printing ordered array
print("Ordered array: " + str(unordered_array))